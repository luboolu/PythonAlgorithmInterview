#리트코드 937 Reorder Log File
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_str = []
        logs_num = []

        for l in logs:
            l_split = l.split(" ")
            identifier = l_split.pop(0)
            s = "".join(l_split)

            if s.isalpha():
                logs_str.append(l)
            else:
                logs_num.append(l)

        logs_str.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return logs_str + logs_num

sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))