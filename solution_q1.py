# DS442 Project 1
# Nick Malloy and Aaryan Bavishi
# September 8 2023

import random
import math
import copy

class Node:

    def __init__(self, state, parent=None, children=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.action = action
        self.cost = cost
        self.name = random.randint(-1000, 1000)

    def __repr__(self):
        return "Node " + str(self.name)

def euclidean(state, goal):
    heuristic_value = 0

    for tile in state:
        current_tile = int(tile) if tile != "_" else 0  # Convert blank to 0
        current_position = state.index(tile)
        goal_position = goal.index(tile)

        # Calculate the row and column of the current and goal positions
        current_row, current_col = divmod(current_position, 3)
        goal_row, goal_col = divmod(goal_position, 3)

        # Calculate straight-line (Euclidean) distance and add it to the heuristic value
        distance = math.sqrt((current_row - goal_row) ** 2 + (current_col - goal_col) ** 2)
        heuristic_value += distance

    return heuristic_value

def manhatten(start,goal):
  dis = 0
  for tile in start:
    if tile!="_":
        dis  += abs(start.index(tile)%3 - goal.index(tile)%3) + abs(start.index(tile)//3 - goal.index(tile)//3)
  return dis

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
        moves.append("Up")
        moves.append("Down")
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

def addChildren(node):                                      # edits the node.children attribute and appends all the states, actions, and costs of the children
    node.children = []                                      # uses available moves to return possible moves at the certain node.state
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

def DFS_Search(node, goal):
    print("The solution of Q1.1(DFS) is:")
    visited = []
    visited.append(node.state)
    while node.state != goal:                                       # will run until node is at goal state
        foundAlready = False
        addChildren(node)                                           # adds children to node.children
        for child in node.children:                                 # iterates through each of the nodes children
            if child[0] not in visited:                             # finds the first child of the node that hasn't been visited yet
                newNode = Node(child[0], node, None, child[1])      # creates a node for the child
                node = newNode                                      # sets this child as the current node
                visited.append(node.state)                          # adds this nodes state/position to the list of visited states
                foundAlready = True                                 # changes the boolean to let us know we can stop iterating through
                break
        if not foundAlready:                                        # if we go through all of the nodes children and all of them have been visited, we will pop the current node and restart with the next deepest node
            node = node.parent
    print(','.join(trackingPath(node)))
    
def BFS1(node, goal):
    print("The solution of Q1.2(BFS) is:")
    start_node = node
    visited = set()
    open = []
    open.append(start_node)
    while open:
        current_node = open.pop(0)
        visited.add(tuple(current_node.state))

        if current_node.state == goal:
            print(','.join(trackingPath(current_node)))
            return

        addChildren(current_node)
        for child in current_node.children:
            if tuple(child[0]) not in visited:
                child_node = Node(child[0], current_node, None, child[1])
                open.append(child_node)

def queueCost(queue):                   # returns the node in the queue with the least cost
    minCost = 1000000
    for item in queue:
        if item.cost < minCost:
            minCost = item.cost
    return minCost

def UCS_search(node, goal):
    print("The solution of Q1.3(UCS) is:")
    visited = []
    queue = []
    goalNode = Node(None, None, None, None, 10000000)               # decoy goal_node, it'll be replaced as soon as we find a goal state
    visited.append(node.state)
    queue.append(node)
    while queueCost(queue) < goalNode.cost:                         # we only want this search to stop, when the cost of the items in the queue are all greater than our lowest goal state
        addChildren(node)                                           # because this means we've found the most optimal solution
        for child in node.children:                                 # expanding the node to the queue as node objects
            if child[0] not in visited:                             # eliminates redundancy
                queue.append(Node(child[0], node, None, child[1], node.cost + 1))
        for item in queue:                                          # searches the queue until it finds a node with the least cost
            if item.cost == queueCost(queue):
                queue.remove(item)
                visited.append(item.state)
                node = item
                break
        if node.state == goal and node.cost < goalNode.cost:        # if we find a goal node of less cost, we will change the current goalNode
            goalNode = node
    print(','.join(trackingPath(node)))

def aStarManhattan(start, goal):
    print("The solution of Q1.4(A*) is:")
    open = []
    closed = set()
    open.append((0, start))  # Start with a cost of 0 for the initial state
    current_node = start
    while current_node.state != goal:
        g_value = 0
        addChildren(current_node)
        for child in current_node.children:
            if tuple(child[0]) not in closed:
                child_node = Node(child[0], current_node, None, child[1])
                h_value = manhatten(current_node.state, goal)  # Heuristic value
                f_value = g_value + h_value
                open.append((f_value, child_node))
                closed.add(tuple(child_node.state))
                g_value+=1

        open.sort(key=lambda x: x[0])
        _, current_node = open.pop(0)

    print(','.join(trackingPath(current_node)))
    return

def aStarStraight(start, goal):
    print("The solution of Q1.5(A*) is:")
    open = []
    closed = set()
    open.append((0, start))  # Start with a cost of 0 for the initial state
    current_node = start
    while current_node.state != goal:
        g_value = 0
        addChildren(current_node)
        for child in current_node.children:
            if tuple(child[0]) not in closed:
                child_node = Node(child[0], current_node, None, child[1])
                h_value = euclidean(current_node.state, goal)  # Heuristic value
                f_value = g_value + h_value
                open.append((f_value, child_node))
                closed.add(tuple(child_node.state))
                g_value+=1

        open.sort(key=lambda x: x[0])
        _, current_node = open.pop(0)

    print(','.join(trackingPath(current_node)))
    return

with open('input') as f:                                # reading in current state of puzzle
    lines = f.readlines()
start = lines[0].split(",")
goal_state = ["_","1","2","3","4","5","6","7","8"]

example = Node(start)
DFS_Search(example, goal_state)
print()
BFS1(example, goal_state)
print()
UCS_search(example, goal_state)
print()
aStarManhattan(example, goal_state)
print()
aStarStraight(example, goal_state)