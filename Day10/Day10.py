import pandas as pd

# input = "example.txt"
input = "input.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]
    
cyc = -1
X = X_prev = 1
cycle_list, X_list, command_list = [], [], []

for cycle, line in enumerate(lines):
    command = line.split(" ")
    X_prev = X
    if len(command) > 1:
        X_prev = X
        for i in range(2):
            cyc+=1
            cycle_list.append(cyc)
            X_list.append(X_prev)
            command_list.append(command)
        X += int(command[1])
    else:
        cyc+=1
        cycle_list.append(cyc)
        X_list.append(X_prev)
        command_list.append(command)
    
df = pd.DataFrame({"Cycles":cycle_list, "X":X_list, "Command":command_list})
df["Signal_strength"] = df["Cycles"] * df["X"]

print(df[0:50])
interesting_signals = [20, 60, 100, 140, 180, 220]

print(sum([df[df.index == i]["Signal_strength"].values for i in interesting_signals]))
