# Hunter Leise
# CSCI-3202 Problem Set 4
# Problem 4.1


import random
import math


class Perceptron:
    def __init__(self, num_inputs, correct_func, bias):
        self.num_inputs = num_inputs
        self.correct = correct_func
        self.bias = bias
        self.weights = self.initialize_weights(self, num_inputs, -1, 1)
        self.errors = 0

    @staticmethod
    def initialize_weights(self, num_weights, range_min, range_max):
        weights = []
        for _ in range(num_weights):
            weights.append(random.uniform(range_min, range_max))
        return weights

    @staticmethod
    def prediction(self, output):
        return True if output >= 0.5 else False

    def train(self, iterations, learning_rate):
        for i in range(iterations):
            if i % 250 == 0:  # print weights every 250 iterations
                print(self.weights)
            inputs = [random.randint(0, 1) for _ in range(self.num_inputs)]
            output = self.sig_output(inputs)
            if self.prediction(self, output) != get_correct(inputs):
                self.errors += 1
                derivative = output * (1.0 - output)
                error = self.correct(inputs) - output
                self.update(learning_rate, error, derivative, inputs)

    def sig_output(self, inputs):
        weighted_sum = self.bias
        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]
        return 1.0 / (1.0 + math.exp(-weighted_sum))

    def update(self, learning_rate, error, derivative, inputs):
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (learning_rate * error * derivative * inputs[i])


def get_correct(inputs):
    """
    Returns the correct output (and function of inputs a and c)
    given a list of inputs.

    Args:
        inputs (integer list): list of integer inputs 0 or 1

    Returns:
        1 for True, 0 for False

    """
    return int(inputs[0] and inputs[2])


def all_correct(perceptron):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                output = perceptron.sig_output([i, j, k])
                prediction = perceptron.prediction(perceptron, output)
                print(i, j, k, output)
                if prediction != get_correct([i, j, k]):
                    return False
    return True


if __name__ == '__main__':
    perceptron = Perceptron(3, get_correct, -1)
    perceptron.train(8000, 1.0)
    print(all_correct(perceptron))
    print(perceptron.errors)
