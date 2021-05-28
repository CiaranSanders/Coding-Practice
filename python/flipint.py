# Ciaran Sanders
# Date: October 8, 2019
# flip the user inputed integer

class flipInt(object):

    def flip_int(self):
        """Flips the inputed integer."""
        while True:
            negative = False
            user_input = input("Please enter an integer (q to quit): ")

            try:
                int(user_input)
            except:
                print("Please enter a valid integer")
                continue

            if user_input == 'q':
                break

            # remove negative sign
            if user_input[0] == '-':
                negative = True
                user_input = user_input[1:]

            # reverse the input
            user_input = user_input[::-1]

            # add back negative sign
            if negative is True:
                user_input = '-' + user_input

            print("Flipped int: ", user_input)


if __name__ == "__main__":
    flipInt().flip_int()
