# Hunter Leise
# CSCI-3202 Problem Set 3
# Problem 3.3

import csv
from math import log2


# Returns the headers, cities, and data from the given csv file
def get_data_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames[1:]
        cities = []
        data = []
        for row in reader:
            cities.append(row['city'])
            data.append([row[headers[0]], row[headers[1]], row[headers[2]],
                         row[headers[3]], int(row[headers[4]]),
                         int(row[headers[5]]), float(row[headers[6]]),
                         row[headers[7]]])
        return headers, cities, data


# Returns the entropy
def entropy(cities, weight):
    counts = label_count(cities)
    total = float(len(cities))
    p_yes = counts['yes'] / total
    p_no = counts['no'] / total
    ent_yes = -p_yes * log2(p_yes) if p_yes != 0 else 0
    ent_no = -p_no * log2(p_no) if p_no != 0 else 0
    return weight * (ent_yes + ent_no)


# Returns the information gain from a query
def info_gain(left, right, current_uncertainty):
    weight_left = float(len(left)) / (len(left) + len(right))
    weight_right = float(len(right)) / (len(left) + len(right))
    total_entropy = entropy(left, weight_left) + entropy(right, weight_right)
    return current_uncertainty - total_entropy


# Leaf node that represents yes or no
class LeafNode:
    def __init__(self, cities):
        self.predictions = label_count(cities)


# Represents a node that splits the data on a question
class QueryNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


# Used to query given examples
class Question:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    # Query if the given example is true for this question
    def is_true(self, example):
        val = example[self.attribute]
        if isinstance(val, int) or isinstance(val, float):  # if number
            return val >= self.value
        else:  # if not a number
            return val == self.value

    def __str__(self):  # Used to print the question
        if isinstance(self.value, int) or isinstance(self.value, float):
            return "Is %s >= %s?" % (headers[self.attribute], str(self.value))
        else:
            return "Is %s == %s?" % (headers[self.attribute], str(self.value))


# Returns the number of cities with each label
def label_count(cities):
    num_labels = {'yes': 0, 'no': 0}
    for city in cities:
        label = city[-1]  # label is the last attribute
        num_labels[label] += 1
    return num_labels


# Check if the question is true for each given city
# Returns a list of the true and false cities
def partition(cities, question):
    true_cities = []
    false_cities = []
    for city in cities:
        if question.is_true(city):
            true_cities.append(city)
        else:
            false_cities.append(city)
    return true_cities, false_cities


# Return the best question and its information gain
def get_best_question(cities):
    best_question = None
    best_gain = 0
    num_attributes = len(headers) - 1

    for attribute in range(0, num_attributes):
        values = set([city[attribute] for city in cities])  # unique values
        for val in values:
            question = Question(attribute, val)

            # split data
            true_rows, false_rows = partition(cities, question)
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue  # skip if data doesn't split

            # get info gain for this attribute
            current_uncertainty = entropy(cities, 1)
            gain = info_gain(true_rows, false_rows, current_uncertainty)
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_question, best_gain


# Recursively builds the decision tree
def build_tree(cities):
    question, gain = get_best_question(cities)

    if gain == 0:  # means it must be a leaf node
        return LeafNode(cities)

    # Recursively builds child branches
    true_cities, false_cities = partition(cities, question)
    true_branch = build_tree(true_cities)
    false_branch = build_tree(false_cities)

    return QueryNode(question, true_branch, false_branch)


# Recursively print the decision tree
def print_tree(node, spacing=""):
    # Base case: leaf node
    if isinstance(node, LeafNode):
        prediction = max(node.predictions, key=node.predictions.get)
        print(spacing + "Predict %s" % prediction)
        return

    # Print question
    print(spacing + str(node.question))

    # True branch
    print(spacing + '  True:')
    print_tree(node.true_branch, spacing + "    ")

    # False branch
    print(spacing + '  False:')
    print_tree(node.false_branch, spacing + "    ")


# Classify a given city
def classify(city, node):
    # Base case: leaf node
    if isinstance(node, LeafNode):
        return node.predictions

    # General case: query node
    if node.question.is_true(city):
        return classify(city, node.true_branch)
    else:
        return classify(city, node.false_branch)


# Returns the prediction for a given classification
# Note that if two values have the same probability,
# it will only return the first
def get_prediction(counts):
    return max(counts, key=counts.get)


if __name__ == '__main__':
    # Get data from training and test csv files
    headers, training_cities, training_data = \
        get_data_from_csv('trainingData.csv')
    _, test_cities, test_data = get_data_from_csv('testData.csv')

    # Use the classifier to build a tree
    tree = build_tree(training_data)
    print_tree(tree)

    # Predict the test cases
    for i in range(0, len(test_data)):
        print("City: %s. Actual: %s. Predicted: %s" %
              (test_cities[i], test_data[i][-1],
               get_prediction(classify(test_data[i], tree))))
