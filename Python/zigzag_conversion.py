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
        row = 0
        if numRows > len(s) | (numRows == 0) | len(s) == 0:
            return s
        while row < numRows:
            # for x in range(row, len(s), inc1):
            #     zigzag = zigzag + s[x]
            type = 0
            x = row
            inc2 = 2*row
            if numRows != 1:
                inc1 = numRows + (numRows - 2) - inc2
            else:
                inc1 = numRows
            zigzag = zigzag + s[x]
            print("inc1" , inc1)
            print("inc2" , inc2)
            print("=====")
            while x < len(s):
                # print(x)
                if type == 0:
                    type = 1
                    #do inc 1
                    if inc1 == 0:
                        continue

                    else:
                        x = x + inc1
                        if x < len(s):
                            zigzag = zigzag + s[x]
                elif type == 1:
                    type = 0
                    #do inc 2
                    if inc2 == 0:
                        continue

                    else:
                        x = x + inc2
                        if x < len(s):
                            zigzag = zigzag + s[x]
            row = row + 1

        return zigzag


if __name__ == "__main__":
    s = input("Enter string: ")
    numRows = int(input("Enter number of rows: "))
    Z = Zigzag()
    print(Z.convert(s, numRows))
