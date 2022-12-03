input = "input.txt"
# input = "example.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]
enc = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
print(sum([enc[i] for i in lines]))
