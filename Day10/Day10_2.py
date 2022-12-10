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
image = ["."]*len(df)

idx = 0
offset = 0
for cycles, X in zip(df["Cycles"], df["X"]):
    if abs(X-idx) in [0,1]:
        image[cycles] = "#"
    if idx == 40:
        idx = 0
        offset+=40
    idx+=1

image = "".join(image)
for i in range(len(image)):
    if i%40 == 0:
        print(image[i-40:i])