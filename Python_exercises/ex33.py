i = 0
numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1

#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")
# for num in numbers:
#     print(num)


def while_loop(num, increment):
    i = 0
    numbers = []
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for number in numbers:
        print(number)
