# Ciaran Sanders
# 10/10/2019
# Leetcode problem. Given a string and a set number of rows, convert the
# string to "zigzag" form. Example/ string = "ZIGZAGME" rows = 3, then the
# zig zag form is "ZAIZGEGM", which we can get by writing out the original
# string as such: Z   A
#                 I Z G E
#                 G   M
# and then combining each row together (row 1 + row 2 + row 3) to create the
# zig-zaged string


class Zigzag(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = ""  # string to be returned
        row = 0  # current row

        if numRows >= len(s) | (numRows == 0) | len(s) == 0:
            return s

        while row < numRows:
            x = row
            type = 0  # determines typ of increment to do; 0->inc1, 1->inc2
            inc2 = 2*row

            if numRows != 1:
                inc1 = numRows + (numRows - 2) - inc2
            else:
                inc1 = numRows

            zigzag += s[x]
            while x < len(s):
                # do increment 1
                if type == 0:
                    type = 1
                    if inc1 != 0:
                        x += inc1
                        if x < len(s):
                            zigzag += s[x]
                # do increment 2
                elif type == 1:
                    type = 0
                    if inc2 != 0:
                        x += inc2
                        if x < len(s):
                            zigzag += s[x]
            row += 1

        return zigzag


if __name__ == "__main__":
    s = input("Enter string: ")
    numRows = int(input("Enter number of rows: "))
    Z = Zigzag()
    print(Z.convert(s, numRows))


# My Solution involves using two different typed of increments to iterate
# across the pattern created by the zig zag. It is a fairly complicated solution
# to try and describe in a text document, but essentially if you draw out
# some zig zagged strings, you will notice each row follows a pattern of
# incrementing by two different intervals on every other character (with respect
# to the indices of the string)
