the_count = [1, 2, 3, 4, 5]

fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list.
for number in the_count:
    print(f'This is count {number}')

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too.
for i in change:
    print(f'I got {i}')

# We can also build lists. Start with an empty one.
elements = []

# Then use the range function to do 0 to 5 counts.
for i in range(0, 5):
    print(f"Adding {i} to the list.")
    # Append is a function that lists understand.
    elements.append(i)

# Now we can print them out too.
for i in elements:
    print(f"Element was: {i}")
