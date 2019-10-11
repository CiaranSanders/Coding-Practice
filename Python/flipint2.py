# Ciaran Sanders
# Date: October 8, 2019
# flip the inputed integer, formatted for submission on leet code
#test
class flipInt(object):

    def reverse(self, x: int) -> int:
        """Flips the inputed integer."""
        negative = False

        strx = str(x)

        # remove negative sign
        if strx[0] == '-':
            negative = True
            strx = strx[1:]

        # reverse the input
        strx = strx[::-1]

        # add back negative sign
        if negative is True:
            strx = '-' + strx

        return int(strx)

if __name__ == "__main__":
    num = flipInt().reverse(1234)
    print(num)
