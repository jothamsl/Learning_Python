class Node:
    def __init__(self, state, parent, action):
        # Core properties
        self.state = state  # Represents formal definition of state
        self.parent = parent  # Parent Node of the current Node (state)
        self.action = action  # The action taken that got to this Node
        self.cost = self._calc_cost()  # Cost getting to this Node

    def _calc_cost(self):
        """Calculate cost of traversing graph to this Node"""
        current_parent = self.parent
        current_cost = 0
        while current_parent != None:
            current_parent = current_parent.parent
            current_cost += 1
        return current_cost 


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

if __name__ == "__main__":
    node1 = Node(0, None, None)
    node2 = Node(1, node1, 0)
    node3 = Node(0, node1, 1)
    node4 = Node(1, node3, 2)
    print(node4.parent)
    print(node4.cost)
