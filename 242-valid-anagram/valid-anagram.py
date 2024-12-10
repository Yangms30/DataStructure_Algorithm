class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            char = s[i]
            print(char)
            if s[i] not in t:
                return False
            else:
                t = t.replace(f'{s[i]}','',1)
        
        return not t