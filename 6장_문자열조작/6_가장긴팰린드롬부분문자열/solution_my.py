class Solution:
    def longestPalindrome(self, s: str) -> str:
        can = []
        palindrome = []
        for i, a in enumerate(s):
            for j, b in enumerate(s):
                slc = s[i: j + 1]

                if slc != "":
                    for c in slc:
                        reverse = ""

                        for i in range(len(slc)):
                            reverse += slc[-1 - i]

                        if slc == reverse:
                            palindrome.append(slc)

        palindrome.sort(key=lambda x: len(x), reverse=True)

        return palindrome[0]