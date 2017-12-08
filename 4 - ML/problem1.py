# Hunter Leise
# CSCI-3202 Problem Set 4
# Problem 4.1


import random
import math


class Perceptron:
    """
    Represents a perceptron and all of the methods necessary to train it.

    Attributes:
        num_inputs (int): number of inputs to the perceptron
        correct (function([list of inputs]) --> bool): function that returns
            the correct output given a list of inputs. Used for training.
        bias (float): initial perceptron bias
        weights (list of float): list of input weights
    """
    def __init__(self, num_inputs, correct_func, bias):
        self.num_inputs = num_inputs
        self.correct = correct_func
        self.bias = bias
        self.weights = self.initialize_weights(self, num_inputs, -1, 1)

    @staticmethod
    def initialize_weights(self, num_weights, range_min, range_max):
        """
        Randomize initial weights before training.

        Args:
            num_weights (int): number of weights to create
            range_min (int): minimum weight for randomization
            range_max (int): maximum weight for randomization

        Returns:
            list of floats: list of weights for each input
        """
        weights = []
        for _ in range(num_weights):
            weights.append(random.uniform(range_min, range_max))
        return weights

    @staticmethod
    def prediction(self, output):
        """
        Takes a sigmoid output value and returns its corresponding
        boolean value.

        Args:
            output (float): sigmoid activation value
        Returns:
            bool: True if output >= 0.5
                False otherwise
        """
        return True if output >= 0.5 else False

    def train(self, iterations, learning_rate):
        """
        Train the perceptron for the given number of iterations.

        Args:
            iterations (int): number of training iterations
            learning_rate (float): learning rate
        Returns:
            None
        """
        for i in range(iterations):
            if i % 250 == 0:  # print weights every 250 iterations
                print(self.weights)
            inputs = [random.randint(0, 1) for _ in range(self.num_inputs)]
            output = self.sig_output(inputs)
            if self.prediction(self, output) != get_correct(inputs):
                derivative = output * (1.0 - output)
                error = self.correct(inputs) - output
                self.update(learning_rate, error, derivative, inputs)

    def sig_output(self, inputs):
        """
        Calculate sigmoid activation function output

        Args:
            inputs (list of int): list of binary inputs
        Returns:
            float: sigmoid activation value
        """
        weighted_sum = self.bias
        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]
        return 1.0 / (1.0 + math.exp(-weighted_sum))

    def update(self, learning_rate, error, derivative, inputs):
        """
        Update the weights using the perceptron update function

        Args:
            learning_rate (float): learning rate
            error (float): calculated error
            derivative (float): sigmoid derivative
            inputs (list of int): list of perceptron binary inputs
        Returns:
            None
        """
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + \
                              (learning_rate * error * derivative * inputs[i])

def get_correct(inputs):
    """
    Return the 'and' function of inputs 1 and 3.

    Args:
        inputs (list of int): list of binary inputs
    Returns:
        int: 1 for True (inputs 1 and 3 are both 1)
            0 for False (either inputs 1 or 3 are 0)
    """
    return int(inputs[0] and inputs[2])


def all_correct(perceptron):
    """
    Check if all possible 3 input combinations return the expected values.

    Args:
        perceptron (Perceptron): perceptron class instance
    Returns:
        bool: True if all input possibilities return the expected values,
            False otherwise.
    """
    for i in range(2):
        for j in range(2):
            for k in range(2):
                output = perceptron.sig_output([i, j, k])
                prediction = perceptron.prediction(perceptron, output)
                if prediction != get_correct([i, j, k]):
                    return False
    return True


if __name__ == '__main__':
    perceptron = Perceptron(3, get_correct, -1)
    perceptron.train(8000, 1.0)
    print(all_correct(perceptron))
