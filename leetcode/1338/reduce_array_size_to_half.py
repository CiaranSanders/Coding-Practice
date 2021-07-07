from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        half = len(arr) / 2
        num = 0
        total = 0
        for val, count in count.most_common():
            total += count
            num += 1
            if total >= half:
                return num
        return 0 


if __name__ == '__main__':
    sol = Solution()
    tests = [
        [7,7,7,7,7,7],  # answer: 1
        [1,2,3,4,5],  # answer: 3
        [1,2,3,4],  # answer: 2
        [1000,1000,1,1],  # answer: 1
        [1000,1000,1,2],  # answer: 1
        [],  # answer: None ? or 0?
        [1],  # answer: 1
        [3,4,5,6,7,6,4,2,1,2,2,2,3,45],  # answer: 3
        [1234,1234],  # answer: 1
    ]
    for test in tests:
        result = sol.minSetSize(test)
        print(result)

