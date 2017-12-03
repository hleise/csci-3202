# Hunter Leise
# CSCI-3202 Problem Set 4
# Problem 4.2

import random


class City:
    def __init__(self):
        self.neighbors = [0] * 6 + [1] * 27 + [2] * 27
        random.shuffle(self.neighbors)
        self.vacant = [i for i, x in enumerate(self.neighbors) if x == 0]

    def iterate(self, iterations):
        for iteration in range(iterations):
            if iteration % 20 == 0:
                print(self.neighbors)

            dissatisfied = []
            for i in range(len(self.neighbors)):
                if self.neighbors[i] != 0 and not self.is_satisfied(i):
                    dissatisfied.append(i)
            if len(dissatisfied) == 0:
                print("all satisfied")
                break
            else:
                rand_dis = random.choice(dissatisfied)
                self.neighbors[self.vacant[0]] = self.neighbors[rand_dis]
                self.neighbors[rand_dis] = 0
                self.vacant.pop(0)
                self.vacant.append(rand_dis)

    def is_satisfied(self, house):
        same_neighbors = 0
        for i in range(1, 3):
            if self.neighbors[(house + i) % len(self.neighbors)] == self.neighbors[house]:
                same_neighbors += 1
            if self.neighbors[(house - i) % len(self.neighbors)] == self.neighbors[house]:
                same_neighbors += 1
        return same_neighbors >= 2


if __name__ == '__main__':
    city = City()
    city.iterate(400)
    print(city.neighbors)
