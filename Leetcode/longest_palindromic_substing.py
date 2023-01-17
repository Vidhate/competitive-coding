# https://leetcode.com/problems/longest-palindromic-substring/

# O(n) solution - https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm 


import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<=1:
            return s

        n = len(s)
        dp = np.zeros([n,n], dtype=np.int8)

        longest, length = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                longest, length = i, 2
            else:
                dp[i][i+1]=False

        for k in range(3,n+1):
            for i in range(n-k+1):

                j = i+k-1
                if s[j]==s[i] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    longest, length = i, k
                else:
                    dp[i][j]=0

        #print(dp)

        return s[longest:longest+length]


    def longestPalindrome2(self, s: str) -> str:
        
        if len(s)<=1:
            return s

        n = len(s)
        dp = np.zeros([n,n], dtype=np.int8)

        longest, length = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                longest, length = i, 2
            else:
                dp[i][i+1]=False

        for k in range(3,n+1):
            for i in range(n-k+1):

                j = i+k-1
                if s[j]==s[i] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    longest, length = i, k
                else:
                    dp[i][j]=0

        #print(dp)

        return s[longest:longest+length]

s = Solution()
inp = "abcdcba"
print(s.longestPalindrome(inp))