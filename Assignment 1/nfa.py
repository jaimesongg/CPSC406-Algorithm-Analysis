# a class for NFAs
# modify as needed
class NFA :

    # init the NFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # non-deterministic transition function
        self.q0 = q0 # initial state
        self.F = F # final states
   
   # print the data of the NFA
    def __repr__(self) :
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the NFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w) :
        current_states = {self.q0}
        for symbol in w:
            next_states = set()
            for state in current_states:
                if state in self.delta and symbol in self.delta[state]:
                    next_states.update(self.delta[state][symbol])
            current_states = next_states
        return any(state in self.F for state in current_states)

    def to_DFA(self):
        """Convert this NFA to an equivalent DFA using subset construction."""
        from dfa import DFA
        def epsilon_closure(states):
            """Compute the epsilon closure of a set of states."""
            stack = list(states)
            closure = set(states)
            while stack:
                state = stack.pop()
                if "" in self.delta.get(state, {}):
                    for next_state in self.delta[state][""]:
                        if next_state not in closure:
                            closure.add(next_state)
                            stack.append(next_state)
            return closure

        def move(states, symbol):
            """Compute the set of states reachable from `states` on `symbol`."""
            next_states = set()
            for state in states:
                if symbol in self.delta.get(state, {}):
                    next_states.update(self.delta[state][symbol])
            return next_states

        initial_closure = frozenset(epsilon_closure({self.q0}))
        dfa_states = {initial_closure}
        dfa_delta = {}
        unprocessed = [initial_closure]
        dfa_final_states = set()

        while unprocessed:
            current = unprocessed.pop()
            dfa_delta[current] = {}

            for symbol in self.Sigma:
                next_set = epsilon_closure(move(current, symbol))
                if next_set:
                    next_frozenset = frozenset(next_set)
                    dfa_delta[current][symbol] = next_frozenset
                    if next_frozenset not in dfa_states:
                        dfa_states.add(next_frozenset)
                        unprocessed.append(next_frozenset)

            if current & self.F:
                dfa_final_states.add(current)

        return DFA(
            {frozenset(s) for s in dfa_states},
            self.Sigma,
            {frozenset(k): {sym: frozenset(v) for sym, v in trans.items()} for k, trans in dfa_delta.items()},
            initial_closure,
            dfa_final_states
        )