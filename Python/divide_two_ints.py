# Ciaran Sanders
# Date: October 15, 2019
# Given two integers, dividen and divisor, divide them and return the
# quotient without using multiplication, division and modulos. Assume ints
# are 32-bit, and the divisor is non-zero. Returns max int value on overflow:
# 2^31 - 1

# TODO need to deal with  overflows

class Solution:
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0

        # get the sign of the what the result will be
        sign = -1 if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)) else 1

        dividend = abs(dividend)  # numerator
        divisor = abs(divisor)  # denominator

        quotient = 0

        # count how many times divisor can fit into dividend
        while dividend >= divisor:
            quotient += 1
            dividend -= divisor

        # add the appropriate sign to the result
        quotient = quotient if sign == 1 else -quotient

        return quotient



if __name__ == "__main__":
    sol = Solution()
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    q = sol.divide(dividend, divisor)
    print(q)
