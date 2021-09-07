class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin = []  ##영문자와 숫자로만 이루어진 input

        for i in s:
            if i.isalnum():
                origin.append(i.lower())

        while len(origin) > 1:
            if origin.pop(0) != origin.pop():
                return False

        return True
