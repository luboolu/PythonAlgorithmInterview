#리트코드 819 Most Common Word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.split(" ")
        print(words)
        dic = []

        for i in range(len(banned)):
            banned[i] = banned[i].lower()

        for word in words:
            tmp = ""
            for w in word:
                if w.isalpha():
                    tmp += w.lower()

            if tmp not in banned:
                dic.append(tmp)

        cnt = []
        for d in dic:
            cnt.append(dic.count(d))

        return dic[cnt.index(max(cnt))]