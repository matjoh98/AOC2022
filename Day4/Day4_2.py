input = "input.txt"
# input = "example.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

count = 0
for pair in lines:
    first_lower, first_upper = int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1])
    second_lower, second_upper = int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1])
    first_list, second_list = [i for i in range(first_lower, first_upper + 1)], [i for i in range(second_lower, second_upper + 1)]

    if len(list(set(first_list) & set(second_list))) > 0:
        count += 1
print(count)
