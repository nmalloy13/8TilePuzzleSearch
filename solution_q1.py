# DS442 Project 1
# Nick Malloy and Aaryan Bavishi
# September 8 2023

with open('input') as f:                                # reading in current state of puzzle
    lines = f.readlines()
lines = lines[0].split(",")
goal_state = ["_","1","2","3","4","5","6","7","8"]


class SubNode:

    def __init__(self, state, goal, depth):
        self.state = state
        self.goal = goal
        self.depth = depth

class Node:

    def __init__(self, state, goal):
        self.state = state
        self.goal = goal
        self.fringe = []
        self.visited = []
        self.path = ""
        self.depth = 0

    def move_right(self):
        tempState = self.state.copy()
        whereSpace = tempState.index("_")
        tempState[whereSpace] = tempState[whereSpace + 1]
        tempState[whereSpace + 1] = "_"
        currentDepth = self.depth
        self.fringe.append([currentDepth, tempState])

    def move_left(self):
        tempState = self.state.copy()
        whereSpace = tempState.index("_")
        tempState[whereSpace] = tempState[whereSpace - 1]
        tempState[whereSpace - 1] = "_"
        currentDepth = self.depth
        self.fringe.append([currentDepth, tempState])

    def move_up(self):
        tempState = self.state.copy()
        whereSpace = self.state.index("_")
        tempState[whereSpace] = tempState[whereSpace - 3]
        tempState[whereSpace - 3] = "_"
        currentDepth = self.depth
        self.fringe.append([currentDepth, tempState])

    def move_down(self):
        tempState = self.state.copy()
        whereSpace = self.state.index("_")
        tempState[whereSpace] = tempState[whereSpace + 3]
        tempState[whereSpace + 3] = "_"
        currentDepth = self.depth
        self.fringe.append([currentDepth, tempState])

    def depthUp(self):
        self.depth += 1

    def depthDown(self):
        self.depth -= 1

    def expansion(self):
        freeSpace = self.state.index("_")
        self.depthUp()
        if freeSpace == 0:  # can move down or right
            self.move_right()
            self.move_down()
        elif freeSpace == 1:  # can move left, down, right
            self.move_left()
            self.move_down()
            self.move_right()
        elif freeSpace == 2:  # can move left or down
            self.move_left()
            self.move_down()
        elif freeSpace == 3:  # can move up, right, or down
            self.move_up()
            self.move_right()
            self.move_down()
        elif freeSpace == 4:  # can move any direction
            self.move_left()
            self.move_up()
            self.move_right()
            self.move_down()
        elif freeSpace == 5:  # can move left, up, or down
            self.move_left()
            self.move_up()
            self.move_right()
        elif freeSpace == 6:  # can move up or right
            self.move_up()
            self.move_right()
        elif freeSpace == 7:  # can move left, up, or right
            self.move_left()
            self.move_up()
            self.move_right()
        elif freeSpace == 8:  # can move left or up
            self.move_left()
            self.move_up()
        self.deepestNode()

    def visitedYet(self):
        if self.state in self.visited:
            self.fringe.remove([self.depth, self.state])
            return True
        else:
            self.visited.append(self.state)
            return False

    def deepestNode(self):
        for item in self.fringe:
            if item[0] == self.depth:
                self.state = item[1]
                self.fringe.remove([self.depth,self.state])
                return
        self.depth -= 1

    def DFS_Search(self):
        while self.state != self.goal:
            while self.visitedYet():
                self.deepestNode()
            self.expansion()
        return self.state


example = Node(lines, goal_state)
example.DFS_Search()
