from nfa import NFA

# Define A1
A1 = NFA(
    {"q0", "q1"},
    {"0", "1"},
    {
        "q0": {"0": {"q0", "q1"}, "1": set()},
        "q1": {"1": {"q0"}, "0": set()}
    },
    "q0",
    {"q1"}
)

# Define A2
A2 = NFA(
    {"q0", "q1", "q2"},
    {"0", "1"},
    {
        "q0": {"0": {"q0", "q1"}, "1": {"q0"}},
        "q1": {"1": {"q2"}, "0": set()},
        "q2": {"0": {"q2"}, "1": {"q2"}}
    },
    "q0",
    {"q2"}
)

# Define A3
A3 = NFA(
    {"q0", "q1", "q2"},
    {"0", "1"},
    {
        "q0": {"0": {"q1"}, "1": {"q0"}},
        "q1": {"1": {"q2"}},
        "q2": {"0": {"q2"}, "1": {"q2"}}
    },
    "q0",
    {"q0", "q1"}  # q0 and q1 are final states
)

# Define A4
A4 = NFA(
    {"q0", "q1", "q2", "q3", "q4"},
    {"0", "1"},
    {
        "q0": {"1": {"q1"}, "0": {"q0"}},
        "q1": {"0": {"q2"}, "1": {"q2"}},
        "q2": {"0": {"q3"}, "1": {"q3"}},
        "q3": {"0": {"q4"}, "1": {"q4"}},
        "q4": {"0": {"q4"}, "1": {"q4"}}
    },
    "q0",
    {"q4"}  # q4 is the final state
)



# Test cases
print("Testing A1")
print(A1.run("110"))  
print(A1.run("000"))  
print(A1.run("101"))  
print(A1.run("11"))   

print("\nTesting A2")
print(A2.run("010"))  
print(A2.run("011"))  
print(A2.run("000")) 
print(A2.run("0010"))

print("\nTesting A3")
print(A3.run("0"))    
print(A3.run("01"))   
print(A3.run("011"))  
print(A3.run("10"))   

print("\nTesting A4")
print(A4.run("1010")) 
print(A4.run("1100")) 
print(A4.run("1"))    
print(A4.run("0000")) 
