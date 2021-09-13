#리트코드 819 Most Common Word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.split(" ")
        print(words)
        dic = []

        banned = [b.lower() for b in banned]

        #b,b,b,b 처럼 공백 없이 나뉜 문자를 찾지 못함
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