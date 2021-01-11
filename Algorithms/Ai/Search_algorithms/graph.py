class Node:
    def __init__(self, state, parent, action):
        # Core properties
        self.state = state  # Represents formal definition of state
        self.parent = parent  # Parent Node of the current Node (state)
        self.action = action  # The action taken that got to this Node
        self.cost = 0  # Cost To get to this Node

    def calc_cost(self):
        """Calculate cost of traversing graph to this Node"""
        current_parent = self.parent
        while current_parent != None:
            current_parent = current_parent.parent
            self.cost += 1
        return self.cost


class StackFrontier:
    def __init__(self):
        self.frontier = [] 

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty:
            raise Exception("Empty Frontier!")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueFrontier(StackFrontier):
    def remove(self):
        if self.empty:
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[0:]
            return node

def main():
    node1 = Node()


if __name__ == "__main__":
    main()
