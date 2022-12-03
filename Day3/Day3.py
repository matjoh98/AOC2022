input = "input.txt"
# input = "example.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

alphabet_map = {**{chr(96 + i): ord(chr(96 + i)) - 96 for i in range(1, 27)}, **{chr(96 - 26 + i).upper(): ord(chr(96 - 26 + i)) - 96 + 26 for i in range(27, 53)}}
print(sum([(alphabet_map[set(rucksack[0 : int(len(rucksack) / 2)]).intersection(set(rucksack[int(len(rucksack) / 2) : :])).pop()]) for rucksack in lines]))
