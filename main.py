#Class State 
class State:
    #initialize our State object with main variables : name // is the state an initial state or a final state ? 
    def __init__(self,name,isInitial = False,isFinal=False):

        self.name = name
        # Declaring an Empty dictionary that will hold {"symbol": "nextState"} pairs   
        self.transitions = {}

        self.isInit = isInitial
        self.isFinal = isFinal
        
    
    #add transition to the transitions dictionary where symbol is key and target is the value
    def addTransition(self, symbol, target):
        self.transitions[symbol] = target;


    #check if it is possible to transit with a symbol to another state and return that state
    def transition(self, symbol):
        if symbol  in self.transitions.keys():

            return self.transitions[symbol]
        else:
            return None

  
    def getState(self):
        return "State's name : "+ self.name +" is Initial :" + self.isInit+ "  is Final:" +self.isFinal
    
    def setState(self,name,isInitial = False,isFinal=False):
         self.name  = name   
         self.isInit=isInitial
         self.isFinal= isFinal

    def getTransitions(self):
        return "State " + self.name +" transitions are :" + self.transitions
    
# Automate class A.K.A AFD
class Automate :

     #initialize Automate with its alphabet 
     def __init__(self,alphabet ):
        self.currentState = None
        self.alphabet = alphabet
     

     def getAlphabet(self):
        return    

     #check if the Automate accept a symbol first  
     def validate_symbol(self,symbol):
        if symbol not in self.alphabet:
            return False
        return True    
    # initialize current state indicating the start of the Automate
     def initState(self,State):
        self.currentState =  State
    
    #transition from current state to next state with a symbol 
     def transition ( self,symbol)   :
        self.currentState = self.currentState.transition(symbol)
        if (self.currentState ==None) : return False
        return True

     def getCurrentState(self) :
        return self.currentState
     def setCurrentState(self,state) :
        self.currentState = state

# main 
word = "aaabbb"

AFD =  Automate({"a","b"})

#declaring states
state0 = State("0",True)
state1 = State("1")
state2 = State("2",False,True)

#adding Transitions
state0.addTransition('a',state2)
state0.addTransition('b',state1)

state1.addTransition('a',state0)
state1.addTransition('b',state2)

state2.addTransition('a',state2)
state2.addTransition('b',state0)

#initialize the start of the Automate
AFD.initState(state0)

#validation
errorFound = False
notAccepted = False
for i in word :
    #check first if symbol is known by the Automate
    if(not AFD.validate_symbol(i)):
        notAccepted = True
        print("This Automate doesn't accept this type of symbol: "+i+"// Automate's alphabet is = ", AFD.alphabet)
        break;
    #check if transition is possible with the symbol
    currentSymbol = i 
    if not AFD.transition(currentSymbol):
        errorFound=True
        break;


#result
if (not errorFound and not notAccepted and AFD.getCurrentState().isFinal==True):
    print(word + " is accepted by the Automate")
else : 
    print(word + " is not accepted by the Automate")    
 


     