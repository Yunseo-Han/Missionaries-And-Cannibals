from state import State

class Main:
    """Class that sets up and finds the solution to the cannibal missionary problem"""

    
    def __init__(self):
        self.path = [] # list that stores the solution path
    

    # uses depth-first search to find the solution to the cannibal missionary problem
    def dfs(self):
        start = State(0, 0, False, "none")  # no missionaries, cannibals, or boat crossed
        goal = State(3, 3, True, None)      # all missionaries, cannibals, and boat crossed

        actions = ["1c", "2c", "1m", "2m", "1c1m"]  # possible actions that can be taken from a state
        visited = set()                             # hashset storing states that have already been explored
        stack = []

        # depth-first search algorithm 
        stack.append(start)
        while (len(stack)):
            currentState = stack.pop()
            self.path.append(currentState)

            if currentState not in visited:
                if currentState==goal:                  # check if currentState is the goal
                    break
                elif not currentState.validState():     # if currentState it not valid, move onto next stack element
                    visited.add(currentState)
                    self.path.pop()
                    continue
                else:                                   # if currentState is valid but not the goal, state needs to be expanded
                    visited.add(currentState)           

                for a in actions:                       # expand the current state 
                    if currentState.prevAction!=a:      # prevent loop of going back and fourth with same action
                        stack.append(currentState.takeAction(a))

            else:   # currentState has been explored and failed before
                self.path.pop()


    # print path to the solution of the cannibal missionary problem
    def printPath(self):
        step = 1
        for p in self.path:
            print(str(step) + ". \t" + p.actionToString() + " => " + p.stateToString())
            step += 1




test = Main()
test.dfs()
test.printPath()






