def prepare_stack(input_stack):
    with open(input_stack) as f:
        lines_stack = [i.replace("\n", "").split() for i in f.readlines()]
    dic = {}
    for i in lines_stack:
        dic = {**dic, **{i[0]: i[1::]}}
    return dic

# input_stack = "example_stack.txt"
input_stack = "stack.txt"

# input = "example.txt"
input = "input.txt"

with open(input) as f:
    lines = [i.replace("\n", "") for i in f.readlines()]

stack_dict = prepare_stack(input_stack)
for i in lines:
    sentence = i.split()
    times = int(sentence[1])
    source = sentence[3]
    destination = sentence[5]
    for k in stack_dict[source][-times:]:
        stack_dict[destination].append(k)
        stack_dict[source].pop()

new = []
for i in stack_dict:
    new.append(stack_dict[i].pop().replace("[", "").replace("]", ""))
print(str(new).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace(" ", ""))
