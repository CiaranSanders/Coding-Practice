# Ciaran Sanders
# Date: October 8, 2019
# Second attemp at the problem as described in flipInt.py, however done in
# fewer lines
while True:
    input = raw_input("Please enter an integer (q to quit): ")
    size = len(input)
    negative = False

    if input == 'q':
        break

    if input[0] == '-':
        negative = True
        input = input[1:]

    # reverse the input
    input = input[::-1]

    if negative is True:
        input = '-' + input

    print "Flipped int: " , input
