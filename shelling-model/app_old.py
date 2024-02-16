# class Agent:
#     def __init__(self, type, pos, tolerancy, model):
#         self.type = type
#         self.pos_x, self.pos_y = pos
#         self.tolerancy = tolerancy
#         self.model = model
#
#     # def get_neighbors(self, pos_x, pos_y):
#     #     return [self.model.grid[row_d + pos_x][col_d + pos_y]
#     #             for col_d in [-1, 0, 1]
#     #             if (0 <= (col_d + pos_y) < len(self.model.grid)) or (col_d == 0 and row_d == 0)
#     #             for row_d in [-1, 0, 1]
#     #             if 0 <= (row_d + pos_x) < len(self.model.grid)]
#
#     def check_happiness(self):
#         same_type = 0
#         other_type = 0
#         if self.pos_y > 0 and self.pos_x > 0 and self.model.grid[self.pos_y - 1][self.pos_x - 1] != 0:  # северо-запад
#             if self.model.grid[self.pos_y - 1][self.pos_x - 1].type == self.type:
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_x > 0 and self.model.grid[self.pos_y][self.pos_x - 1] != 0:  # север
#             if self.model.grid[self.pos_y][self.pos_x - 1].type == self.type:
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y < (self.model.grid_size - 1) and self.pos_x > 0 and self.model.grid[self.pos_y + 1][
#             self.pos_x - 1] != 0:  # северо-восток
#             if self.model.grid[self.pos_y + 1][self.pos_x - 1].type == self.type:
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y > 0 and self.model.grid[self.pos_y - 1][self.pos_x] != 0:  # запад
#             if self.model.grid[self.pos_y - 1][self.pos_x].type == self.type:
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y < (self.model.grid_size - 1) and self.model.grid[self.pos_y + 1][self.pos_x] != 0:
#             if self.model.grid[self.pos_y + 1][self.pos_x].type == self.type:  # восток
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y > 0 and self.pos_x < (self.model.grid_size - 1) and self.model.grid[self.pos_y - 1][
#             self.pos_x + 1] != 0:
#             if self.model.grid[self.pos_y - 1][self.pos_x + 1].type == self.type:  # юго-запад
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y > 0 and self.pos_x < (self.model.grid_size - 1) and self.model.grid[self.pos_y][
#             self.pos_x + 1] != 0:
#             if self.model.grid[self.pos_y][self.pos_x + 1].type == self.type:  # юг
#                 same_type += 1
#             else:
#                 other_type += 1
#         if self.pos_y < (self.model.grid_size - 1) and self.pos_x < (self.model.grid_size - 1) and \
#                 self.model.grid[self.pos_y + 1][self.pos_x + 1] != 0:
#             if self.model.grid[self.pos_y + 1][self.pos_x + 1].type == self.type:  # юго-восток
#                 same_type += 1
#             else:
#                 other_type += 1
#         if other_type >= self.tolerancy:
#             return False
#         return True
# class App:
#     def __init__(self, grid_size, density, f):
#         self.global_happiness = 0
#         self.grid_size = grid_size
#         self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
#         self.ratio = floor((grid_size ** 2) * density) // 2
#         self.empty_spaces = []
#         for agent_type in [1, 2]:
#             for _ in range(self.ratio):
#                 pos_x, pos_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
#                 while self.grid[pos_x][pos_y] != 0:
#                     pos_x, pos_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
#                 # self.grid[pos_x][pos_y] = Agent(agent_type, (pos_x, pos_y), f)
#                 self.grid[pos_y][pos_x] = agent_type
#         for y in range(grid_size):
#             for x in range(grid_size):
#                 if self.grid[y][x] == 0:
#                     self.empty_spaces.append((y, x))
#                 else:
#                     self.grid[y][x] = Agent(self.grid[y][x], (x, y), f, self)
#
#     def update(self):
#         # actions = 0
#         unhappy_agents = []
#         for row in self.grid:
#             for item in row:
#                 if item != 0:
#                     if not (item.check_happiness()):
#                         unhappy_agents.append((item))
#         new_grid = self.grid.copy()
#         print(new_grid)
#         for agent in unhappy_agents:
#             new_place = random.choice(self.empty_spaces)
#             del self.empty_spaces[self.empty_spaces.index(new_place)]
#             self.empty_spaces.append((agent.pos_y, agent.pos_x))
#             new_grid[agent.pos_y][agent.pos_x], new_grid[new_place[0]][new_place[1]] = 0, agent
#         self.grid = new_grid
#
#     def return_cur_state(self):
#         return self.grid, self.empty_spaces
#
#     def return_grid_visual(self):
#         color_grid = [[i.type if i != 0 else 0 for i in x] for x in self.grid]
#         return color_grid
