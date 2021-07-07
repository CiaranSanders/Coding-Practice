from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # convert nxm matrix into rxc
        n = len(mat[0])  # columns TODO handle if matrix is empty
        m = len(mat)  # rows
        if n * m != r * c:
            return mat
        else:
            arr = [[]]
            for row in range(0, m):
                for col in range(0, n):
                    arr[-1].append(mat[row][col])
                    if len(arr[-1]) == c and len(arr) != r:
                        arr.append([])
            return arr


if __name__ == '__main__':
    solution = Solution()
    # arr = solution.matrixReshape([[1,2,3,4]], 2, 2)
    arr = solution.matrixReshape([[1,2],[3,4]], 2, 4)
    print(arr)
