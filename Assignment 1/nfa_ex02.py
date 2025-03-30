import dfa
import nfa

def __main__():
    A1 = dfa.DFA(
        {"q0", "q1"},
        {"0", "1"},
        {
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q1", "1": "q0"}
        },
        "q0",
        {"q1"}
    )

    A2 = dfa.DFA(
        {"q0", "q1", "q2"},
        {"0", "1"},
        {
            "q0": {"0": "q1", "1": "q0"},
            "q1": {"0": "q2", "1": "q1"},
            "q2": {"0": "q0", "1": "q2"}
        },
        "q0",
        {"q2"}
    )

    A3 = dfa.DFA(
        {"q0", "q1", "q2"},
        {"0", "1"},
        {
            "q0": {"0": "q1", "1": "q0"},
            "q1": {"1": "q2", "0": "q1"},
            "q2": {"0": "q2", "1": "q2"}
        },
        "q0",
        {"q2"}
    )

    A4 = dfa.DFA(
        {"q0", "q1", "q2", "q3", "q4"},
        {"0", "1"},
        {
            "q0": {"1": "q1"},
            "q1": {"0": "q2"},
            "q2": {"0": "q3", "1": "q3"},
            "q3": {"0": "q4", "1": "q4"},
            "q4": {"0": "q4", "1": "q4"}
        },
        "q0",
        {"q4"}
    )

    # convert 
    NFA1 = A1.to_NFA()
    NFA2 = A2.to_NFA()
    NFA3 = A3.to_NFA()
    NFA4 = A4.to_NFA()

    # test 
    print("Testing NFA1 (converted from DFA1)")
    print(NFA1.run("0"))   # Expect False
    print(NFA1.run("1"))   # Expect True
    print(NFA1.run("10"))  # Expect False
    print(NFA1.run("11"))  # Expect True

    print("\nTesting NFA2 (converted from DFA2)")
    print(NFA2.run("00"))  # Expect False
    print(NFA2.run("000")) # Expect True
    print(NFA2.run("01"))  # Expect False
    print(NFA2.run("001")) # Expect True

    print("\nTesting NFA3 (converted from DFA3)")
    print(NFA3.run("00"))  # Expect False
    print(NFA3.run("01"))  # Expect False
    print(NFA3.run("011")) # Expect True

    print("\nTesting NFA4 (converted from DFA4)")
    print(NFA4.run("1"))   # Expect False
    print(NFA4.run("10"))  # Expect False
    print(NFA4.run("1000"))# Expect True

__main__()
