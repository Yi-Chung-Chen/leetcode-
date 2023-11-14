class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0])-ord('a')+int(coordinates[1])+1)%2
  # https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/
