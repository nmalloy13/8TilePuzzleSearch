# DS442 Project 1
# Nick Malloy and Aaryan Bavishi
# September 8 2023

with open('input') as f:                                # reading in current state of puzzle
    lines = f.readlines()
start = lines[0].split(",")
goal_state = ["_","1","2","3","4","5","6","7","8"]

class Node:

    def __init__(self, state, parent=None, children=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.action = action
        self.cost = cost

def trackingPath(node):                             # will run when you find a path to the goal state, walks back the path
    actionPath = []
    while node != None:
        if node.action != None:
            actionPath.append(node.action)
        node = node.parent
    return actionPath[::-1]


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
    node.children = []
    moves = availableMoves(node)
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
    path.append(node)
    visited.append(node.state)
    while node.state != goal:
        foundAlready = False
        addChildren(node)
        for child in node.children:
            if child[0] not in visited:
                newNode = Node(child[0], node, None, child[1])
                node = newNode
                path.append(node)
                visited.append(node.state)
                foundAlready = True
                break
        if not foundAlready:
            path.pop()
            node = node.parent
    print(','.join(trackingPath(node)))
    print(node.state)

def BFS_Search(node, goal):
    print("The solution of Q1.2(BFS) is:")
    path = []
    visited = []
    queue = []
    path.append(node)
    visited.append(node.state)
    while node.state != goal:
        addChildren(node)
        for children in node.children:          # add all children to the queue
            queue.append(children)
        newChild = queue.pop(0)                 # pops most recent node
        while newChild in visited:
            newChild = queue.pop(0)
        newNode = Node(newChild[0], node, None, newChild[1])
        path.append(newNode)
        visited.append(newNode.state)
        node = newNode
    print(','.join(trackingPath(node)))
    print(node.state)

def uniformCost_search(node, goal):
    print("The solution of Q1.3(UCS) is:")
    path = []
    visited = []
    queue = []
    cost = 0
    minCost = 1000000
    while node.state != goal:
        addChildren(node)
        cost += 1
        for children in node.children:      # add all children to the queue
            children.append(cost)
            queue.append(children)
        for tempNode in queue:                  # finding smallest cost in the queue
            if tempNode.cost < minCost:
                minCost = tempNode.cost
        for tempNode in queue:              # find the first item in the queue with this cost for expansion
            if tempNode.cost == minCost:
                newNode = queue.pop(queue.index(tempNode))
                path.append()

    print(','.join(trackingPath(node)))


example = Node(start)
DFS_Search(example, goal_state)
BFS_Search(example, goal_state)