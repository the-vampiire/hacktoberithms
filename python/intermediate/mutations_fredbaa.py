def mutations(inputs):
    item_a = set(inputs[0].lower())
    item_b = set(inputs[1].lower())

    return item_b.intersection(item_a) == item_b

print(mutations(["hello", "Hello"]))
print(mutations(["hello", "hey"]))
print(mutations(["Alien", "line"]))