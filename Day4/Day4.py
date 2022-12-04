input = "input.txt"
# input = "example.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

count = 0
for pair in lines:
    first_lower, first_upper = int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1])
    second_lower, second_upper = int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1])
    if (first_lower >= second_lower) & (first_upper <= second_upper) | (second_lower >= first_lower) & (second_upper <= first_upper):
        count += 1

print(count)
