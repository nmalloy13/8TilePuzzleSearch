# DS442 Project 1
# Nick Malloy and Aaryan Bavishi
# September 8 2023

with open('input') as f:                                # reading in current state of puzzle
    lines = f.readlines()
start = lines[0].split(",")
goal_state = ["_","1","2","3","4","5","6","7","8"]

class Node:

    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __repr__(self):
        if self.action != None:
            return self.action
        else:
            return


def availableMoves(node):                          # returns all possible moves at a given state
    moves = []                                      # order of moves is down, left, right, up
    blank_index = node.state.index("_")
    if blank_index == 0:
        moves.append("Down")
        moves.append("Right")
    elif blank_index == 1:
        moves.append("Down")
        moves.append("Left")
        moves.append("Right")
    elif blank_index == 2:
        moves.append("Down")
        moves.append("Left")
    elif blank_index == 3:
        moves.append("Down")
        moves.append("Left")
        moves.append("Right")
    elif blank_index == 4:
        moves.append("Down")
        moves.append("Left")
        moves.append("Right")
        moves.append("Up")
    elif blank_index == 5:
        moves.append("Down")
        moves.append("Left")
        moves.append("Up")
    elif blank_index == 6:
        moves.append("Right")
        moves.append("Up")
    elif blank_index == 7:
        moves.append("Left")
        moves.append("Right")
        moves.append("Up")
    elif blank_index == 8:
        moves.append("Left")
        moves.append("Up")
    return moves

def addChildren(node):
    moves = availableMoves(node)
    node.children = []
    for move in moves:
        blankSpace = node.state.index("_")
        if move == "Left":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace - 1] = tempNode[blankSpace - 1], tempNode[blankSpace]
            node.children.append([tempNode, tempNode[blankSpace] + "R"])
        elif move == "Right":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace + 1] = tempNode[blankSpace + 1], tempNode[blankSpace]
            node.children.append([tempNode, tempNode[blankSpace] + "L"])
        elif move == "Up":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace - 3] = tempNode[blankSpace - 3], tempNode[blankSpace]
            node.children.append([tempNode, tempNode[blankSpace] + "D"])
        elif move == "Down":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace + 3] = tempNode[blankSpace + 3], tempNode[blankSpace]
            node.children.append([tempNode, tempNode[blankSpace] + "U"])
    return

def DFS_Search(node, goal):
    print("The solution of Q1.1(DFS) is:")
    path = []
    visited = []
    actionPath = []
    path.append(node)
    visited.append(node.state)
    while node.state != goal:
        foundAlready = False
        addChildren(node)
        for child in node.children:
            if child[0] not in visited:
                newNode = Node(child[0], node, child[1])
                node = newNode
                path.append(node)
                actionPath.append(node.action)
                visited.append(node.state)
                foundAlready = True
                break
        if not foundAlready:
            path.pop()
            actionPath.pop()
            node = node.parent
    print(','.join(actionPath))

def BFS_Search(node, goal):
    print("The solution of Q1.2(BFS) is:")
    path = []
    visited = []
    actionPath = []
    queue = []
    path.append(node)
    visited.append(node.state)
    while node.state != goal:
        addChildren(node)
        for children in node.children:          # add all children to the queue
            queue.append(children)
        newChild = queue.pop(0)
        while newChild in visited:
            newChild = queue.pop(0)
        newNode = Node(newChild[0], node, newChild[1])
        path.append(newNode)
        actionPath.append(newNode.action)
        visited.append(newNode.state)
        node = newNode
    print(','.join(actionPath))

def aStarSearch(state, goal):
    

example = Node(start)
BFS_Search(example, goal_state)