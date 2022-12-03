input = "input.txt"
# input = "example.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

alphabet_map = {**{chr(96 + i): ord(chr(96 + i)) - 96 for i in range(1, 27)}, **{chr(96 - 26 + i).upper(): ord(chr(96 - 26 + i)) - 96 + 26 for i in range(27, 53)}}
total_sum = []
for rucksack in lines:
    length = len(rucksack)
    compartment1, compartment2 = rucksack[0 : int(length / 2)], rucksack[int(length / 2) : :]
    total_sum.append((alphabet_map[set(compartment1).intersection(set(compartment2)).pop()]))

print(sum(total_sum))
