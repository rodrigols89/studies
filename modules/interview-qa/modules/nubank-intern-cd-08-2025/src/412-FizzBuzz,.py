from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:  # O(1)
        result = []                           # O(1)
        for i in range(1, n + 1):             # O(n) × O(1) = O(n)
            if i % 3 == 0 and i % 5 == 0:     # O(1)
                result.append("FizzBuzz")     # O(1)
            elif i % 3 == 0:                  # O(1)
                result.append("Fizz")         # O(1)
            elif i % 5 == 0:                  # O(1)
                result.append("Buzz")         # O(1)
            else:                             # O(1)
                result.append(str(i))         # O(1)
        return result                         # O(1)

if __name__ == '__main__':
    fb = Solution()
    result = fb.fizzBuzz(15)
    print(result)
