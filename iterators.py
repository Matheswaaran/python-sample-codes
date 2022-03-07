#!/usr/bin/python

numbers = [1, 4, 23]

print(dir(numbers))
print("\n================================================\n")

try:
    value = numbers.__iter__()
    print(value)

    item1 = next(value)
    print(item1)

    item2 = next(value)
    print(item2)

    item3 = next(value)
    print(item3)

    item4 = next(value)
    print(item4)

except StopIteration:
    print("End of the list. No more items available in the list")

print("\n================================================\n")

while True:
    try:
        item1 = next(value)
        print(item)
    except StopIteration:
        break
        print("End of the list. No more items available in the list")
