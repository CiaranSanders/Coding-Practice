import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # this is the bad solution! doesn't leverage the fact that the matrix is sorted
        # return sorted([num for sublist in matrix for num in sublist])[k-1]

        # create a heap, storing tuples of (val, index)
        n = len(matrix)
        heap = [(matrix[0][0], (0, 0))]
        val = None
        for _ in range(0, k):
            head = heapq.heappop(heap)
            val = head[0]
            i, j = head[1]
            if i + 1 < n:
                heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        return val


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
        [[[1,2], [1,3]], 2],
        [[[1,2,5], [2,3,4], [4,4,5]], 4],
        [[[1,2,3], [2,5,6], [4,4,5]], 4],
    ]
    for matrix, k in tests:
        print(sol.kthSmallest(matrix, k))

