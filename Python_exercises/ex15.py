# This line imports the arguments from the sys module.
# from sys import argv

# we want to see the script and the filename that we're providing as an argument.
# script, filename = argv

txt = input("Type in a filename here: ")

filename = open(txt)

print(f"Here's your file {txt}: ")
print(filename.read())
filename.close()

# print("Type the filename again: ")
# file_again = input("> ")


# txt_again = open(file_again)
# print(txt_again.read())
# txt_again.close()
