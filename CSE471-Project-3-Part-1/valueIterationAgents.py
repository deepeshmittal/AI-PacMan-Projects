# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.actions = {}
        
        for _ in range(iterations):
            new_stateValues = {}
            new_actionValue = {}
            for state in self.mdp.getStates():
                qvalue_list = []
                possible_actions = mdp.getPossibleActions(state)
                if (len(possible_actions) == 0):
                    new_stateValues[state] = 0                 
                    new_actionValue[state] = None
                else:
                    for action in possible_actions:
                        qvalue_list.append((self.getQValue(state,action),action))
                    vvalue = max(qvalue_list)
                    new_stateValues[state] = vvalue[0]                   
                    new_actionValue[state] = vvalue[1]
                    
            self.values = new_stateValues     
            self.actions = new_actionValue


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        qvalue = 0
        possible_tansition = self.mdp.getTransitionStatesAndProbs(state,action)
        for single_transition in possible_tansition:
            reward = self.mdp.getReward(state, action, single_transition[0])
            probability = single_transition[1]
            utility_value = self.getValue(single_transition[0])
            qvalue = qvalue + (probability * (reward + (self.discount * utility_value)))
        return qvalue
        

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if (len(self.actions) == 0):
            return None
        
        return self.actions[state]
        

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
