# Hunter Leise
# CSCI-3202 Problem Set 4
# Problem 4.2

import random


class City:
    """
    Represents a ring city and the necessary methods for how it operates.

    Attributes:
        neighbors (list of int): list of neighbor types
        vacant (list of int): indexes of vacant homes in the neighbors list.
    """
    def __init__(self):
        self.neighbors = [0] * 6 + [1] * 27 + [2] * 27
        random.shuffle(self.neighbors)
        self.vacant = [i for i, x in enumerate(self.neighbors) if x == 0]

    def iterate(self, iterations):
        """
        Iterate until all neighbors are satisfied or until the maximum
        number of iterations is reached.

        Args:
            iterations (int): Maximum number of times the cycle will be run

        Returns:
            None
        """
        for iteration in range(iterations):
            if iteration % 20 == 0:  # print every 20 iterations
                print(self.neighbors)

            dissatisfied = []
            for i in range(len(self.neighbors)):
                if self.neighbors[i] != 0 and not self.is_satisfied(i):
                    dissatisfied.append(i)
            if len(dissatisfied) == 0:  # Yay! Everyone is satisfied!
                print("all satisfied")
                break
            else:  # Move unsatisfied people to vacant house
                rand_dis = random.choice(dissatisfied)
                self.neighbors[self.vacant[0]] = self.neighbors[rand_dis]
                self.neighbors[rand_dis] = 0
                self.vacant.pop(0)
                self.vacant.append(rand_dis)

    def is_satisfied(self, house):
        """
        Returns whether a given house is satisfied. In other words,
        whether it has at least two neighbors of its own type within
        two houses on either side.

        Args:
            house (int): index for the queried house

        Returns:
             bool: True if satisfied, False if not satisfied
        """
        same_neighbors = 0
        for i in range(1, 3):
            if self.neighbors[(house + i) % len(self.neighbors)] \
                    == self.neighbors[house]:
                same_neighbors += 1
            if self.neighbors[(house - i) % len(self.neighbors)] \
                    == self.neighbors[house]:
                same_neighbors += 1
        return same_neighbors >= 2


if __name__ == '__main__':
    city = City()
    city.iterate(400)
    print(city.neighbors)  # Print final neighborhood
