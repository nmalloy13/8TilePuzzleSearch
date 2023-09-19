# DS442 Project 1
# Nick Malloy and Aaryan Bavishi
# September 8 2023

with open('input') as f:                                # reading in current state of puzzle
    lines = f.readlines()
start = lines[0].split(",")
goal_state = ["_","1","2","3","4","5","6","7","8"]

class Node:

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return self.action

def availableMoves(node):                          # returns all possible moves at a given state
    moves = []
    blank_index = node.state.index("_")
    if blank_index == 0:
        moves.append("Down")
        moves.append("Right")
    elif blank_index == 1:
        moves.append("Right")
        moves.append("Down")
        moves.append("Left")
    elif blank_index == 2:
        moves.append("Down")
        moves.append("Left")
    elif blank_index == 3:
        moves.append("Down")
        moves.append("Right")
        moves.append("Left")
    elif blank_index == 4:
        moves.append("Up")
        moves.append("Down")
        moves.append("Right")
        moves.append("Left")
    elif blank_index == 5:
        moves.append("Down")
        moves.append("Up")
        moves.append("Left")
    elif blank_index == 6:
        moves.append("Right")
        moves.append("Up")
    elif blank_index == 7:
        moves.append("Up")
        moves.append("Right")
        moves.append("Left")
    elif blank_index == 8:
        moves.append("Up")
        moves.append("Left")
    return moves

def addMoves(node):
    moves = availableMoves(node)
    children = []
    for move in moves:
        blankSpace = node.state.index("_")
        if move == "Left":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace - 1] = tempNode[blankSpace - 1], tempNode[blankSpace]
            children.append([tempNode, tempNode[blankSpace] + "R"])
        elif move == "Right":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace + 1] = tempNode[blankSpace + 1], tempNode[blankSpace]
            children.append([tempNode, tempNode[blankSpace] + "L"])
        elif move == "Up":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace - 3] = tempNode[blankSpace - 3], tempNode[blankSpace]
            children.append([tempNode, tempNode[blankSpace] + "D"])
        elif move == "Down":
            tempNode = node.state.copy()
            tempNode[blankSpace], tempNode[blankSpace + 3] = tempNode[blankSpace + 3], tempNode[blankSpace]
            children.append([tempNode, tempNode[blankSpace] + "U"])
    return children

def DFS_Search(node, goal):
    path = []
    visited = []
    path.append(node)
    visited.append(node.state)
    while node.state != goal:
        node.children = addMoves(node)
        for child in node.children:
            if child[0] not in visited:
                newNode = Node(child[0], node, child[1])
                node = newNode
                path.append(node)
                visited.append(node.state)
                break
        path.pop()
        node = node.parent
    return path

example = Node(start)
DFS_Search(example, goal_state)