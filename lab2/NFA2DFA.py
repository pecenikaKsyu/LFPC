import pandas as pd

NFA = {}
states_brut = input("Define the states (separe them by space)\n")
states = states_brut.split(" ")
print("Q = {}".format(states))
nr_states = len(states)
paths_brut = input("Define the paths (separe them by space)\n")
paths = paths_brut.split(" ")
print("S = {}".format(paths))
nr_paths = len(paths)
finals_brut = input("Define the final state/s (separe them by space)\n")
finals = finals_brut.split(" ")
print("F = {}".format(finals))
nr_finals = len(finals)

print("For each state, complete the NFA table")
for i in range(nr_states):
    state = input("state name : ")  # Enter state name eg: A, B, C, q1, q2 ..etc
    NFA[state] = {}  # Creating a nested dictionary
    for j in range(nr_paths):
        path = input("path : ")  # Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reaching_state = [x for x in input().split()]  # Enter all the end states that
        NFA[state][path] = reaching_state  # Assigning the end states to the paths in dictionary

print("\nNFA :- \n")
print(NFA)  # Printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(NFA)
print(nfa_table.transpose())

newbies_list = []
DFA = {}
keys_list = list(NFA.keys())
# Computing first row of DFA transition table
DFA[keys_list[0]] = {}
for y in range(nr_paths):
    var = "".join(NFA[keys_list[0]][
                      paths[y]])
    DFA[keys_list[0]][paths[y]] = var
    if var not in keys_list:
        newbies_list.append(var)
        keys_list.append(var)
# Computing the other rows of DFA transition table
while len(newbies_list) != 0:
    DFA[newbies_list[0]] = {}
    for _ in range(len(newbies_list[0])):
        for i in range(len(paths)):
            aux = []
            for j in range(len(newbies_list[0])):
                aux += NFA[newbies_list[0][j]][paths[i]]
            s = ""
            s = s.join(aux)
            if s not in keys_list:
                newbies_list.append(s)
                keys_list.append(s)
            DFA[newbies_list[0]][paths[i]] = s

    newbies_list.remove(newbies_list[0])

print("\nDFA :- \n")
print(DFA)
print("\nPrinting DFA table :- ")
Table_DFA = pd.DataFrame(DFA)
print(Table_DFA.transpose())

dfa_states = list(DFA.keys())
dfa_terminals = []
for x in dfa_states:
    for i in x:
        if i in finals:
            dfa_terminals.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_terminals)
