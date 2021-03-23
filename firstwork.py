# This is a sample Python script.

massiv = [1, 2, 2, 3, 5, 6, 77, 77, 89]
counter = {}

for elem in massiv:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)





