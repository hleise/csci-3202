# Hunter Leise
# CSCI-3202 Problem Set 3
# Problem 3.3

import csv
from math import log2


# Returns the header array, cities array, and data array from the given csv file
def get_data_from_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames[1:]
        cities = []
        data = []
        for row in reader:
            cities.append(row['city'])
            data.append([row[headers[0]], row[headers[1]], row[headers[2]],
                         row[headers[3]], int(row[headers[4]]), int(row[headers[5]]),
                         float(row[headers[6]]), row[headers[7]]])
        return headers, cities, data


# Returns the number of cities with each label
def label_count(cities):
    num_labels = {'yes': 0, 'no': 0}
    for city in cities:
        label = city[-1]  # label is the last attribute
        num_labels[label] += 1
    return num_labels


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


# Returns the entropy
def entropy(cities, weight):
    counts = label_count(cities)
    total = float(len(cities))
    p_yes = (counts['yes'] / total) if counts['yes'] != 0 else 0
    p_no = (counts['no'] / total) if counts['no'] != 0 else 0
    new_yes = -p_yes * log2(p_yes) if p_yes != 0 else 0
    new_no = -p_no * log2(p_no) if p_no != 0 else 0
    return weight * (new_yes + new_no)


# Returns the information gain from a query
def info_gain(left, right, current_uncertainty):
    weight_left = float(len(left)) / (len(left) + len(right))
    weight_right = float(len(right)) / (len(left) + len(right))
    return current_uncertainty - (entropy(left, weight_left) + entropy(right, weight_right))


# x
def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = entropy(rows, 1)
    n_features = len(rows[0]) - 1  # number of columns

    for col in range(n_features):  # for each feature

        values = set([row[col] for row in rows])  # unique values in the column

        for val in values:  # for each value

            question = Question(col, val)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


# x
class Leaf:
    """A Leaf node classifies data.
    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = label_count(rows)


# x
class Decision_Node:
    """A Decision Node asks a question.
    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


# x
def build_tree(rows):
    """Builds the tree.
    Rules of recursion: 1) Believe that it works. 2) Start by checking
    for the base case (no further information gain). 3) Prepare for
    giant stack traces.
    """

    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
    gain, question = find_best_split(rows)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0:
        return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
    true_rows, false_rows = partition(rows, question)

    # Recursively build the true branch.
    true_branch = build_tree(true_rows)

    # Recursively build the false branch.
    false_branch = build_tree(false_rows)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)


# x
def print_tree(node, spacing=""):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print(spacing + str(node.question))

    # Call this function recursively on the true branch
    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


# x
def classify(row, node):
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.is_true(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


# x
def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


# x
if __name__ == '__main__':
    # Get data from training and test csv files
    headers, training_cities, training_data = get_data_from_csv('trainingData.csv')
    _, test_cities, test_data = get_data_from_csv('testData.csv')

    # Use the classifier to build a tree
    tree = build_tree(training_data)
    print_tree(tree)

    # Predict the test cases
    for i in range(0, len(test_data)):
        print("City: %s. Actual: %s. Predicted: %s" %
              (test_cities[i], test_data[i][-1], print_leaf(classify(test_data[i], tree))))