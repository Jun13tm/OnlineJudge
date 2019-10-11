class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(w1, w2, dic):
            if not w1: return 0
            if not w2: return 1
            for i in range(min(len(w1), len(w2))):
                if dic[w1[i]] == dic[w2[i]]:
                    continue
                elif dic[w1[i]] < dic[w2[i]]:
                    return 0
                else:
                    return 1
            # share same common part
            return 0 if len(w1) < len(w2) else 1

        # Edge case
        if len(words) <= 1: return words
        
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        
        for i in range(1, len(words)):
            if compare(words[i - 1], words[i], dic) == 1:
                return False
        return True
        
        
        