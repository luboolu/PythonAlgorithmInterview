import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

sol = Solution()
print(sol.isPalindrome(""))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
