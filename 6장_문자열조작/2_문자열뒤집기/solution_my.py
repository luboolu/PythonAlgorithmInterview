#리트코드 344 Reverse String
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s = s[::-1]
        s.reverse()
        """
        실제로 배열이 뒤집히긴 하지만, 리트코드에선 에러 발생
        
        """



sol = Solution()
print(sol.reverseString(["H", "E", "l", "l", "o"]))