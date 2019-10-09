# Ciaran Sanders
# Date: October 8, 2019
# First Python program. Given inputed integer, flip the digits.
# Preserve the sign of the number.
while True:
    string = raw_input("Please enter an integer (q to quit): ")
    size = len(string)
    start = 0
    temp = ""
    end = size - 1

    if string == 'q':
        break

    # convert string to list
    list = []
    for s in string:
        list.append(s)

    # if negative, skip minus sign
    if list[0] == "-":
        start = start + 1

    if (size % 2) != 0:
        size = size + 1

    # flip all necessary characters
    for i in range(start, size//2):
        temp = list[i]
        list[i] = list[end]
        list[end] = temp
        end = end - 1

    str = ""
    for l in list:
        str = str + l

    flipped = int(str)

    print "Flipped integer: ", flipped
