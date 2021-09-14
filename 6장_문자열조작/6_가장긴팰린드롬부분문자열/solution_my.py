class Solution:
    def longestPalindrome(self, s: str) -> str:
        can = []

        for i, a in enumerate(s):
            for j, b in enumerate(s):
                slc = s[i: j + 1]

                if slc != "":
                    can.append(slc.lower())

        palindrome = []
        for c in can:
            reverse = ""
            is_palindrome = False

            for i in range(len(c)):
                reverse += c[-1 - i]

            if c == reverse:
                palindrome.append(c)

        palindrome.sort(key=lambda x: len(x), reverse=True)

        return palindrome[0]