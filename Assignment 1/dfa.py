# a class for DFAs
# modify as needed
from nfa import NFA
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function
        self.q0 = q0 # initial state
        self.F = F # final states

    # convert DFA to NFA
    def to_NFA(self):
        return NFA(
            self.Q,
            self.Sigma,
            {state: {symbol: {next_state} for symbol, next_state in transitions.items()} for state, transitions in self.delta.items()},
            self.q0,
            self.F
        )
    
   # print the data of the DFA
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w) :
        state = self.q0
        for symbol in w:
            if symbol in self.delta[state]:
                state = self.delta[state][symbol]
            else:
                return False
        return state in self.F
