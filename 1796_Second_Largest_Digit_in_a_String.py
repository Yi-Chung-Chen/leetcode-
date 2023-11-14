class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for char in s:
            if char.isdigit():
                seen.add(char)
        if len(seen) == 1 or len(seen) == 0:
            return -1
        seen = sorted(seen)
        return int(seen[-2])
  # https://leetcode.com/problems/second-largest-digit-in-a-string/description/
