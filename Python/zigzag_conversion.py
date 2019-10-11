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
        zigzag = ""
        inc = numRows + (numRows - 2)
        row = 0
        for x in range(row, len(s), inc):
            zigzag = zigzag + s[x]

        return zigzag


if __name__ == "__main__":
    s = input("Enter string: ")
    numRows = int(input("Enter number of rows: "))
    Z = Zigzag()
    print(Z.convert(s, numRows))
