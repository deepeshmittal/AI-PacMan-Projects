# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""
   
    loc_stack = Stack()
    visited_node = {}
    parent_child_map = {}
    direction_list = [] 
       
    start_node = problem.getStartState()
    parent_child_map[start_node] = []
    loc_stack.push(start_node)
        
    def traverse_path(parent_node):
        while True:
            map_row = parent_child_map[parent_node]
            if (len(map_row) == 2):
                parent_node = map_row[0]
                direction = map_row[1]
                direction_list.append(direction)
            else:
                break       
        return direction_list
        
    while (loc_stack.isEmpty() == False):
        
        parent_node = loc_stack.pop()
        
        if (problem.isGoalState(parent_node)):
            pathlist = traverse_path(parent_node)
            pathlist.reverse()
            return pathlist
        
        elif (visited_node.has_key(parent_node) == False):
            visited_node[parent_node] = []            
            sucessor_list = problem.getSuccessors(parent_node)
            no_of_child = len(sucessor_list)
            if (no_of_child > 0):          
                temp = 0
                while (temp < no_of_child):
                    child_nodes = sucessor_list[temp]
                    child_state = child_nodes[0];
                    child_action = child_nodes[1];
                    if (visited_node.has_key(child_state) == False):
                        loc_stack.push(child_state)
                        parent_child_map[child_state] = [parent_node,child_action]
                    temp = temp + 1

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    loc_queue = Queue()
    visited_node = {}
    parent_child_map = {}
    direction_list = [] 
       
    start_node = problem.getStartState()
    parent_child_map[start_node] = []
    loc_queue.push(start_node)
        
    def traverse_path(parent_node):
        while True:
            map_row = parent_child_map[parent_node]
            if (len(map_row) == 2):
                parent_node = map_row[0]
                direction = map_row[1]
                direction_list.append(direction)
            else:
                break  
        return direction_list
        
    while (loc_queue.isEmpty() == False):
        
        parent_node = loc_queue.pop()
        
        if (problem.isGoalState(parent_node)):
            pathlist = traverse_path(parent_node)
            pathlist.reverse()
            return pathlist
        
        elif (visited_node.has_key(parent_node) == False):
            visited_node[parent_node] = []            
            sucessor_list = problem.getSuccessors(parent_node)
            no_of_child = len(sucessor_list)
            if (no_of_child > 0):          
                temp = 0
                while (temp < no_of_child):
                    child_nodes = sucessor_list[temp]
                    child_state = child_nodes[0];
                    child_action = child_nodes[1];
                    if (visited_node.has_key(child_state) == False):
                        loc_queue.push(child_state)
                    if (parent_child_map.has_key(child_state) == False):
                        parent_child_map[child_state] = [parent_node,child_action]
                    temp = temp + 1

def uniformCostSearch(problem):
        
    loc_pqueue = PriorityQueue()
    visited_node = {}
    parent_child_map = {}
    direction_list = [] 
    path_cost = 0
       
    start_node = problem.getStartState()
    parent_child_map[start_node] = []
    loc_pqueue.push(start_node,path_cost)
        
    def traverse_path(parent_node):
        while True:
            map_row = parent_child_map[parent_node]
            if (len(map_row) == 3):
                parent_node = map_row[0]
                direction = map_row[1]
                direction_list.append(direction)
            else:
                break       
        return direction_list
        
    while (loc_pqueue.isEmpty() == False):
        
        parent_node = loc_pqueue.pop()
        
        if (parent_node != problem.getStartState()):
            path_cost = parent_child_map[parent_node][2]
                
        if (problem.isGoalState(parent_node)):
            pathlist = traverse_path(parent_node)
            pathlist.reverse()
            return pathlist
        
        elif (visited_node.has_key(parent_node) == False):
            visited_node[parent_node] = []            
            sucessor_list = problem.getSuccessors(parent_node)
            no_of_child = len(sucessor_list)
            if (no_of_child > 0):          
                temp = 0
                while (temp < no_of_child):
                    child_nodes = sucessor_list[temp]
                    child_state = child_nodes[0];
                    child_action = child_nodes[1];
                    child_cost = child_nodes[2];
                    gvalue = path_cost + child_cost
                    if (visited_node.has_key(child_state) == False):
                        loc_pqueue.push(child_state,gvalue)
                    if (parent_child_map.has_key(child_state) == False):
                        parent_child_map[child_state] = [parent_node,child_action,gvalue]
                    else:
                        if (child_state != start_node):
                            stored_cost = parent_child_map[child_state][2]
                            if (stored_cost > gvalue):
                                parent_child_map[child_state] = [parent_node,child_action,gvalue]
                    temp = temp + 1

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    loc_pqueue = PriorityQueue()
    visited_node = {}
    parent_child_map = {}
    direction_list = [] 
    path_cost = 0
    heuristic_value = 0
       
    start_node = problem.getStartState()
    parent_child_map[start_node] = []
    loc_pqueue.push(start_node,heuristic_value)
        
    def traverse_path(parent_node):
        temp = 0
        while True:
            '''print parent_node'''
            map_row = parent_child_map[parent_node]
            if (len(map_row) == 4):
                parent_node = map_row[0]
                direction = map_row[1]
                gvalue = map_row[2]
                fvalue = map_row[3]
                direction_list.append(direction)
                '''print "Gvalue = %d" % gvalue
                print fvalue'''
                '''print "Hueristic = %d" % (fvalue-gvalue)'''
                '''print "Admissible H = %d" % temp'''
                temp = temp + 1
            else:
                break       
        return direction_list
        
    while (loc_pqueue.isEmpty() == False):
        
        parent_node = loc_pqueue.pop()
        
        if (parent_node != problem.getStartState()):
            path_cost = parent_child_map[parent_node][2]
                
        if (problem.isGoalState(parent_node)):
            pathlist = traverse_path(parent_node)
            pathlist.reverse()
            return pathlist
        
        elif (visited_node.has_key(parent_node) == False):
            visited_node[parent_node] = []            
            sucessor_list = problem.getSuccessors(parent_node)
            no_of_child = len(sucessor_list)
            if (no_of_child > 0):          
                temp = 0
                while (temp < no_of_child):
                    child_nodes = sucessor_list[temp]
                    child_state = child_nodes[0];
                    child_action = child_nodes[1];
                    child_cost = child_nodes[2];
                    
                    heuristic_value = heuristic(child_state, problem)
                    gvalue = path_cost + child_cost
                    fvalue = gvalue + heuristic_value
                    
                    if (visited_node.has_key(child_state) == False):
                        loc_pqueue.push(child_state,fvalue)
                    if (parent_child_map.has_key(child_state) == False):
                        parent_child_map[child_state] = [parent_node,child_action,gvalue,fvalue]
                    else:
                        if (child_state != start_node):
                            stored_fvalue = parent_child_map[child_state][3]
                            if (stored_fvalue > fvalue):
                                parent_child_map[child_state] = [parent_node,child_action,gvalue,fvalue]
                    temp = temp + 1


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
