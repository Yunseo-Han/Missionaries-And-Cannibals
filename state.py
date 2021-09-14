
class State:
    """Class describing the current state of the cannibal missionary problem"""


    # cc = number of cannibals crossed; mc = number missionaries crossed; bc = boat crossed true or false; prevAction = action taken to reach this state
    def __init__(self, cc, mc, bc, prevAction):
        self.cc = cc
        self.mc = mc
        self.bc = bc
        self.cnc = 3-cc # cannibals not crossed
        self.mnc = 3-mc # missionaries not crossed
        self.prevAction = prevAction
       

    # takes an action (crossing with the boat) and returns a new state with result
    # actions are described with the following strings: 1m, 2m, 1c, 2c, 1c1m
    # 1m = 1 missionary cross; 2m = 2 missionaries cross; 1c = 1 cannibal cross; 2c = 2 cannibals cross; 1c1m = 1 cannibal and 1 missionary cross
    def takeAction(self, action):
        newState = None
        newCc = self.cc
        newMc = self.mc

        if action == "1m":
            if self.bc:     newMc-=1
            else:           newMc+=1
        elif action == "2m":
            if self.bc:     newMc-=2
            else:           newMc+=2
        elif action == "1c":
            if self.bc:     newCc-=1
            else:           newCc+=1
        elif action == "2c":
            if self.bc:     newCc-=2
            else:           newCc+=2
        elif action == "1c1m":
            if self.bc:     
                newMc-=1
                newCc-=1
            else:
                newMc+=1
                newCc+=1
        else:
            print("ERROR: INVALID ACTION")
            return None
        
        return State(newCc, newMc, not self.bc, action)


    # determines if the current state is valid/legal
    # states are valid if missionaries are safe and the numbers fit the problem
    def validState(self):
        status = True
        if self.cc>self.mc and self.mc!=0:
            status = False
        elif self.cnc>self.mnc and self.mnc!=0:
            status = False
        elif self.cc<0 or self.mc<0 or self.cnc<0 or self.mnc<0:
            status = False
        elif self.cc>3 or self.mc>3 or self.cnc>3 or self.mnc>3:
            status = False
        return status
    

    # returns string information about the current state
    def stateToString(self):
        boatStatus = ""
        if self.bc:
            boatStatus = "crossed"
        else:
            boatStatus = "not crossed"
        return ("[Not crossed: " + str(self.cnc) +" cannibals, " + str(self.mnc) + " missionaries // " + 
                "Crossed: " + str(self.cc) +" cannibals, " + str(self.mc) + " missionaries // " + 
                "Boat status:" + boatStatus + "]")


    # return string information about the action taken to reach this state
    def actionToString(self):
        returnval = ""
        if self.prevAction == "none":
            returnval = "<Start>"
        elif self.prevAction == "1m":
            returnval = "[1 missionary cross]"
        elif self.prevAction == "2m":
            returnval = "[2 missionaries cross]"
        elif self.prevAction == "1c":
            returnval = "[1 cannibal cross]"
        elif self.prevAction == "2c":
            returnval = "[2 cannibals cross]"
        elif self.prevAction == "1c1m":
            returnval = "[1 cannibal and 1 missionary cross]"
        else:
            returnval = "ERROR: INVALID ACTION"
        return returnval


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, State):
            return self.cc==other.cc and self.mc==other.mc and self.bc==other.bc
        return NotImplemented


    def __hash__(self):
        return hash((self.cc, self.mc, self.bc))

