import nfa

def __main__():
    A = nfa.NFA(
        {"q0", "q1", "q2"},
        {"0", "1"},
        {
            "q0": {"0": {"q0", "q1"}, "1": {"q0"}},
            "q1": {"1": {"q2"}},
            "q2": {"0": {"q2"}, "1": {"q2"}}
        },
        "q0",
        {"q2"}
    )

    DFA_A = A.to_DFA()

    A0 = DFA_A

    print("Testing DFA_A (converted from NFA A)")
    print(DFA_A.run("010"))  # Expect False
    print(DFA_A.run("011"))  # Expect True
    print(DFA_A.run("000"))  # Expect False
    print(DFA_A.run("0010"))  # Expect True

__main__()
