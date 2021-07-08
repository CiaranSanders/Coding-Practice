import heapq
import time
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # this is the bad solution! doesn't leverage the fact that the matrix is sorted
        # ok, but this solution actually runs so much faster!!! which is contrary to 
        #   what i thought
        return sorted([num for sublist in matrix for num in sublist])[k-1]

        # create a heap, storing tuples of (val, index)
        # n = len(matrix)
        # heap = [(matrix[0][0], (0, 0))]
        # val = None
        # for _ in range(0, k):
            # head = heapq.heappop(heap)
            # val = head[0]
            # i, j = head[1]
            # if i + 1 < n:
                # temp = (matrix[i + 1][j], (i + 1, j))
                # # its these if statements causing the massive performance decrease
                # if temp not in heap:
                    # heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
            # if j + 1 < n:
                # temp = (matrix[i][j + 1], (i, j + 1))
                # # its these if statements causing the massive performance decrease
                # if temp not in heap:
                    # heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        # return val

        # testing a solution i found
        # yeah this is waaay faster than my min heap solution, but still slower than my
        #   original solution, I wonder why this is? It must be due to some efficient
        #   sorting algorithm in place by python
        # heap = []
        # val = None
        # for row in matrix:
            # for element in row:
                # heapq.heappush(heap, element)

        # for _ in range(k):
            # val = heapq.heappop(heap)
        # return val 



if __name__ == '__main__':
    sol = Solution()
    tests = [
        [[[1,5,9],[10,11,13],[12,13,15]], 8],
        [[[-5]], 1],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 10
        ],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 6
        ],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 5
        ],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 1
        ],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 25
        ],
        [[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            ], 18
        ],
        [[[1,2], [1,3]], 2],  # 1
        [[[1,2,5], [2,3,4], [4,4,5]], 4],  # 3
        [[[1,2,3], [2,5,6], [4,4,5]], 4],  # 3
        [[[1,3,5],[6,7,12],[11,14,14]], 6],  # 11
    ]
    for matrix, k in tests:
        print(sol.kthSmallest(matrix, k))
    # test massive matrix
    arr = [[0 for i in range(10000)] for j in range(10000)]
    arr[-1][-1] = 9
    start = time.time()
    print(sol.kthSmallest(arr, 100000000))
    end = time.time()
    print(f'time elapsed: {end - start}')

