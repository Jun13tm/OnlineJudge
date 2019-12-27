'''
    • Complexity:
        ○ O(nlogn) - involve sorting
    • Topics:
        ○ sort (custom key)
题目出的稀烂，但是解法值得学习。第一，split()可以只执行一次。第二，custom key function会
把log拆解成一个tuple，比方说"let2 own kit dig" => (0, 'own ket dig', 'let2')。
那么sorted再拆解完每一个log后，会按照tuple内的顺序依次compare解决conflict，由小到大。
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_key(log):
            # Only split once
            id_, content = log.split(" ", 1)
            # If content contains letters
            if content[0].isalpha():
                # First compare 优先级，then content, then id_
                return (0, content, id_)
            else:
                # 数字优先级低于字母，且数字log之间不比大小，因此保留原顺序。
                return (1,)
        
        return sorted(logs, key = custom_key)