class Node:
    """A representation of a maze."""

    def __init__(self, state, parent, action):
        """intialize the parameters"""
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    """depth first search"""

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.pop()
            return node

class QueneFrontier(StackFrontier):
    '''breadth first search'''
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
    else:
        node = self.frontier.pop(0)
        return node


class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise.Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            rasie.Exception("maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None


    def print(self):
        solution = self.solution[1] if self.solution is not None else None 
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print(" ", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state

        # all possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        # ensure actions are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append(action, (r, c))
            except IndexError:
                continue
        return result

    def solve(self):
        """finds a solution to maze, if one exists"""

        # keep track of number of states explored
        self.num_explored = 0

        # initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # initialize an empty explored set
        self.explored = set()

        # keep looping until solution found
        while True:

            # if nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # if node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                calls = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # mark node as explored
            self.explored.add(node.state)

            # add neighbours to frontier
            for action, state, in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)



m = Maze(sys.argv[1])
print("Maze: ")
m.print()
print("solving...")
m.solve()
print("States Explored: ", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored)
