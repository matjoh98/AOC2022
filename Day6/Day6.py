# input = "example.txt"
input = "input.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()][0]

print(["First marker after character PART 1: {}".format(i + 4) for i in range(len(lines)) if len(set(lines[i : i + 4])) == 4][0])
print(["First marker after character PART 2: {}".format(i + 14) for i in range(len(lines)) if len(set(lines[i : i + 14])) == 14][0])
