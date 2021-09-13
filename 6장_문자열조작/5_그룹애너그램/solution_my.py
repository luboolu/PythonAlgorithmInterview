class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_split = []

        for s in strs:
            strs_split.append(sorted(list(s)))

        set_strs = list(set([tuple(set(strs_split)) for strs_split in strs_split]))
        print(set_strs)
        answer = []
        for ss in set_strs:
            tmp = []
            for i, s in enumerate(strs_split):
                if ss == s:
                    tmp.append(strs[i])
            answer.append(tmp)

        return answer
