from copy import *

def milkDFS(start):
    stack = [(start, [start])]
    visited = []

    while stack:
        (state, path) = stack.pop()
        print(getState(state))
        visited.append(getState(state))
        children = getChildren(state)
        for child in children:
            child2 = deepcopy(child)
            child2[0], child2[1] = child2[1], child2[0]

            if (child not in visited) and (child2 not in visited):
                if child[2].contents == 2 and child[3].contents == 2:
                    return path + [child]
                else:
                    stack.append((child, path + [child]))
    return []

def getChildren(state):
    children = []

    for cupFrom in range(0, len(state)):
        for cupTo in range(0, len(state)):
            if (not state[cupFrom].isEmpty()) and (not state[cupTo].isFull()) and (cupFrom != cupTo):
                childState = deepcopy(state)
                if childState[cupFrom].contents > childState[cupTo].getOpenSpace():
                    childState[cupFrom].contents -= childState[cupTo].getOpenSpace()
                    childState[cupTo].contents = childState[cupTo].capacity
                else:
                    childState[cupTo].contents += childState[cupFrom].contents
                    childState[cupFrom].contents = 0
                children.append(childState)

    return children

def getState(state):
    stateArray = []
    for cup in state:
        stateArray.append(cup.contents)
    return stateArray

class Cup:
    def __init__(self, capacity, contents):
        self.capacity = capacity
        self.contents = contents

    def __eq__(self, other):
        if self.capacity.value == other.capacity.value:
            return True
        else:
            False

    def getOpenSpace(self):
        return self.capacity - self.contents

    def isFull(self):
        return True if self.capacity == self.contents else False

    def isEmpty(self):
        return True if self.contents == 0 else False

def main():
    startingState = [Cup(40, 40), Cup(40, 40), Cup(5, 0), Cup(4, 0)]
    milkDFS(startingState)

main()