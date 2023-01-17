# https://www.interviewbit.com/problems/vowel-and-consonant-substrings/

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        vowels = ['a','e','i','o','u']
        v, c = [i for i,x in enumerate(A) if x in vowels], [i for i,x in enumerate(A) if x not in vowels]

        vn, vc = len(v), len(c)
        print(vn, vc)

        mod = (1e9)+7
        res = 0
        for i,x in enumerate(A):
            if x in vowels:
                res = (res + (vc % mod)) % mod
                print(vc, res)
                vn-=1
            else:
                res = (res + (vn % mod)) % mod
                print(vn, res)
                vc-=1

        return int(res%mod)
