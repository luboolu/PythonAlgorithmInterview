#리트코드 937 Reorder Log File

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # logs = sorted(logs)
        answer = []
        logs_str = []
        logs_num = []

        print(logs)
        for l in logs:
            l_split = l.split(" ")
            identifier = l_split.pop(0)
            s = "".join(l_split)

            if s.isalpha():
                logs_str.append(l)
            else:
                logs_num.append(l)

            # result.sort(key=lambda x: x["weight"], reverse=True)

        return logs_str + logs_num


sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))