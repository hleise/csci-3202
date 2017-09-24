class ProblemSpace:
    def __init__(self, _startingState, _capacity):
        self.start = _startingState
        self.capacity = _capacity
capacity = [40, 40, 5, 4]

def milkDFS(start):
    stack = [(start, [start])]
    visited = []

    while stack:
        (state, path) = stack.pop()
        visited.append(state)
        children = getChildren(state)
        for child in children:
            child2 = child.copy()
            child2[0], child2[1] = child2[1], child2[0]

            if (child not in visited) and (child2 not in visited):
                if child[2] == 2 and child[3] == 2:
                    return path + [child]
                else:
                    stack.append((child, path + [child])) #DFS
                    # stack.insert(0, (child, path + [child])) # BFS
    return []

def getChildren(state):
    children = []

    for cupFrom in range(0, len(state)):
        for cupTo in range(0, len(state)):
            if (state[cupFrom] > 0) and (not isFull(state, cupTo)) and (cupFrom != cupTo):
                childState = state.copy()
                if childState[cupFrom] > getOpenSpace(childState, cupTo):
                    childState[cupFrom] -= getOpenSpace(childState, cupTo)
                    childState[cupTo] = capacity[cupTo]
                else:
                    childState[cupTo] += childState[cupFrom]
                    childState[cupFrom] = 0
                children.append(childState)

    return children

def isFull(state, index):
    return True if state[index] == capacity[index] else False

def getOpenSpace(state, index):
    return capacity[index] - state[index]

def main():
    startingState = [40, 40, 0, 0]
    print(milkDFS(startingState))

main()