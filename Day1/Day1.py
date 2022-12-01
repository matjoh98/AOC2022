import pandas as pd

with open("input.txt") as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

elfnbr, elfcalories, largest, bank = [], [], 0, 0
for idx, i in enumerate(lines):
    if len(i) > 0:
        bank += int(i)
    if len(i) == 0:
        elfnbr.append(idx)
        elfcalories.append(bank)
        bank = 0
df = pd.DataFrame({"ElfNumber": elfnbr, "ElfCalories": elfcalories})
print(df.sort_values("ElfCalories").tail(3)["ElfCalories"])
