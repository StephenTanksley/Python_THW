print("Mary had a little lamb.")
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?
# line 4 printed out 10 "." and concatenated them all together.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = " " at the end. Try removing it to see what happens.

# end=" " will put these strings on the same line. Removing it will create a line break.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)