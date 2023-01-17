# https://leetcode.com/contest/biweekly-contest-77/problems/count-prefixes-of-a-given-string/

from typing import List
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        if len(s)==0 or len(words)==0:
            return 0
        
        for word in words:
            if len(word)<=len(s) and s.find(word)==0:
                count+=1
        
        return count

s = Solution()
print(s.countPrefixes(["a","b","c","ab","bc","abc"], "abc"))
print(s.countPrefixes(["a","a"], "aa"))