import random
from math import floor
from itertools import product
from pprint import pprint
import numpy as np


#
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
#
#


class App:

    def __init__(self, size, empty_ratio, similarity_threshold, n_neighbors):
        self.size = size
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_neighbors = n_neighbors

        p = [(1 - empty_ratio) / 2, (1 - empty_ratio) / 2, empty_ratio]
        city_size = int(np.sqrt(self.size)) ** 2
        self.city = np.random.choice([-1, 1, 0], size=city_size, p=p)
        self.city = np.reshape(self.city, (int(np.sqrt(city_size)), int(np.sqrt(city_size))))

    def update(self):
        for (row, col), value in np.ndenumerate(self.city):
            agent = self.city[row, col]
            print(self.city)
            if agent != 0:
                neighborhood = self.city[row - self.n_neighbors:row + self.n_neighbors,
                               col - self.n_neighbors:col + self.n_neighbors]
                neighborhood_size = np.size(neighborhood)
                n_empty_houses = len(np.where(neighborhood == 0)[0])
                if neighborhood_size != n_empty_houses + 1:
                    n_similar = len(np.where(neighborhood == agent)[0]) - 1
                    similarity_ratio = n_similar / (neighborhood_size - n_empty_houses - 1.)
                    is_unhappy = (similarity_ratio < self.similarity_threshold)
                    if is_unhappy:
                        empty_houses = list(zip(np.where(self.city == 0)[0], np.where(self.city == 0)[1]))
                        random_house = random.choice(empty_houses)
                        self.city[random_house] = agent
                        self.city[row, col] = 0
