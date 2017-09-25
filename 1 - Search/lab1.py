# Class to represent the problem space
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
                    if child[2] == 2 and child[3] == 2:  # Check if goal state
                        return path + [child]
                    else:  # Append to front or back of stack depending on DFS or BFS
                        stack.append((child, path + [child])) #DFS
                        #stack.insert(0, (child, path + [child])) # BFS
        return []

    # Returns a list of children states for the given state
    def getChildren(self, state):
        children = []

        for cupFrom in range(0, len(state)):
            for cupTo in range(0, len(state)):
                if (state[cupFrom] > 0) and (not self.isFull(state, cupTo)) and (cupFrom != cupTo):
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