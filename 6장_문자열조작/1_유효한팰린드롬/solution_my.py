#리트코드 125.Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin = "" ##영문자와 숫자로만 이루어진 input
        reverse = "" ##origin을 뒤집은 문자

        for i in s:
            if i.isalnum():
                origin += i.lower()

        for i in range(len(origin)):
            reverse += origin[-1 - i]

        if origin == reverse:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(""))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("A man, a plan, a canal: Panama"))