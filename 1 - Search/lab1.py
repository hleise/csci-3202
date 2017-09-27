# Hunter Leise
# CSCI-3202 Lab 1


# Class to represent the problem space
# The starting state and capacity lists should be the same length
class ProblemSpace:
    def __init__(self, _startingState, _capacity):
        self.start = _startingState
        self.capacity = _capacity

    # DFS for the starting state and capacity of the problem space
    # Goal state is when the last two cups both contain 2 quarts
    def milkDFS(self):
        stack = [(self.start, [self.start])]  # Add the starting state to the stack
        visited = []

        while stack:
            (state, path) = stack.pop()
            visited.append(state)
            children = self.getChildren(state)
            for child in children:
                # Check if the version of the state with the first two cups
                # swapped is not in visited. Since both states are equivalent.
                child2 = child.copy()
                child2[0], child2[1] = child2[1], child2[0]

                if (child not in visited) and (child2 not in visited):
                    # Slight optimization such that if a child already exists
                    # in the stack, that must mean there's a faster
                    # way to get there, so skip it.
                    if (not any(child in childPath for childPath in stack)) and \
                       (not any(child2 in child2Path for child2Path in stack)):
                        if child[2] == 2 and child[3] == 2:  # Check if goal state
                            return path + [child]
                        else:
                            stack.append((child, path + [child]))  # DFS
                            # stack.insert(0, (child, path + [child])) # BFS

        return []  # Returns an empty list if there is no solution

    # Returns a list of child states for the given state
    def getChildren(self, state):
        children = []

        # Loop through all possible 'to' and 'from' cups
        for cupFrom in range(0, len(state)):
            for cupTo in range(0, len(state)):
                if (state[cupFrom] > 0) and \
                   (not self.isFull(state, cupTo)) and \
                   (cupFrom != cupTo):
                    childState = state.copy()
                    if childState[cupFrom] > self.getOpenSpace(childState, cupTo):
                        childState[cupFrom] -= self.getOpenSpace(childState, cupTo)
                        childState[cupTo] = self.capacity[cupTo]
                    else:
                        childState[cupTo] += childState[cupFrom]
                        childState[cupFrom] = 0
                    children.append(childState)

        return children

    # Returns whether a cup is full, given a state and the cup's index
    def isFull(self, state, index):
        return True if state[index] == self.capacity[index] else False

    # Returns how much open space a cup has, given a state and the cup's index
    def getOpenSpace(self, state, index):
        return self.capacity[index] - state[index]


problemSpace = ProblemSpace([40, 40, 0, 0], [40, 40, 5, 4])
print(problemSpace.milkDFS())
