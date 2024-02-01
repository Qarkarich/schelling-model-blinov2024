import random
from math import floor
from itertools import product


class Agent:
    def __init__(self, type, pos, tolerancy, model):
        self.type = type
        self.pos_x, self.pos_y = pos
        self.tolerancy = tolerancy
        self.model = model

    def get_neighbors(self, pos_x, pos_y):
        return [self.model.grid[row_d + pos_x][col_d + pos_y]
                for col_d in [-1, 0, 1]
                if (0 <= (col_d + pos_y) < len(self.model.grid)) or (col_d == 0 and row_d == 0)
                for row_d in [-1, 0, 1]
                if 0 <= (row_d + pos_x) < len(self.model.grid)]

    def check_happiness(self):
        same_type = 0
        neighbors = self.get_neighbors(self.pos_x, self.pos_y)
        for i in neighbors:
            if i == self:
                same_type += 1
        if same_type >= self.tolerancy:
            return 1
        return 0


class App:
    def __init__(self, grid_size, density, f):
        self.global_happiness = 0
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.ratio = floor((grid_size ** 2) * density) // 2
        self.empty_spaces = []
        for agent_type in [1, 2]:
            for _ in range(self.ratio):
                pos_x, pos_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
                while self.grid[pos_x][pos_y] != 0:
                    pos_x, pos_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
                # self.grid[pos_x][pos_y] = Agent(agent_type, (pos_x, pos_y), f)
                self.grid[pos_x][pos_y] = agent_type
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y] == 0:
                    self.empty_spaces.append((x, y))
                else:
                    self.grid[x][y] = Agent(self.grid[x][y], (x, y), f, self)

    def update(self):
        for row in self.grid:
            for item in row:
                if item != 0:
                    if item.check_happiness() == 0:
                        new_loc = self.empty_spaces.pop(random.randint(0, len(self.empty_spaces) - 1))
                        self.grid[item.pos_x][item.pos_y], self.grid[new_loc[0]][new_loc[1]] = 0, item
                        self.empty_spaces.append((item.pos_x, item.pos_y))
                        print(self.empty_spaces, len(self.empty_spaces))
                    # self.global_happiness += item.check_happiness()

    def return_cur_state(self):
        return self.grid, self.empty_spaces

    def return_grid_visual(self):
        color_grid = [[i.type if i != 0 else 0 for i in x] for x in self.grid]
        return color_grid
