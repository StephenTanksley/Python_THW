from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

query = input("What's your name?")

print("The script is called: ", script)
print("The first variable is called: ", first)
print("The second variable is: ", second)
print("The third variable is: ", third)

print(f"{query}: Here are your favorite characters - {first}, {second}, {third}.")

print(argv)
