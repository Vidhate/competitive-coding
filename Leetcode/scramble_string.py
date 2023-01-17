# https://leetcode.com/problems/scramble-string/
# st = 12:16; en = 

class Solution:
    def mergeCombinations(self, comb1, comb2):
        result = set()
        for c1 in comb1:
            for c2 in comb2:
                result.add(c1+c2)
                result.add(c2+c1)

        return list(result)

    def possibleScrambles(self, current):
        if len(current)==1:
            return [current]


        level_combinations = []
        for i in range(1,len(current)):
            left, right = current[:i], current[i:]
            sublevel_combinations_left = self.possibleScrambles(left)
            sublevel_combinations_right = self.possibleScrambles(right)
            level_combinations.extend(self.mergeCombinations(sublevel_combinations_left, sublevel_combinations_right))

        return list(set(level_combinations))


    def contains(self, anchor, target):
        anchor_chars, target_chars = {}, {}
        for c1, c2 in zip(anchor, target):
            if anchor_chars.get(char, None) is None:
                anchor_chars[char] = 1
            else:
                anchor_chars[char]+=1

            if target_chars.get(char, None) is None:
                target_chars[char] = 1
            else:
                target_chars[char]+=1

        for char, count in anchor_chars.items():
            if target_chars.get(char,None) is None or target_chars[char]!=count:
                return False
        return True


    #def findSubstring(self, anchor, target):


    def isItScrambled(self, anchor, target):
        if not len(anchor)==len(target):
            return False
        if not self.contains(anchor, target):
            return False

        #find substring between target and anchor
        # split left, right of target and anchor 
        # return self.isItScrambled(target_left, anchor_left) or self.isItScrambled(target_right, anchor_left)


    def possibleScrambles2(self, current, target):
        
        if current==target:
            return True

        if len(current)==1:
            return current==target

        for i in range(1, len(current)):
            if sorted(current[:i])==sorted(target[:i]) and sorted(current[i:])==sorted(target[i:]):
                if self.possibleScrambles2(current[:i], target[:i]) and self.possibleScrambles2(current[i:], target[i:]):
                    return True

            if sorted(current[:i])==sorted(target[-i:]) and sorted(current[i:])==sorted(target[:-i]):
                if self.possibleScrambles2(current[i:], target[:-i]) and self.possibleScrambles2(current[:i], target[-i:]):
                    return True

        return False


    def isScramble(self, s1: str, s2: str) -> bool:
        """
        allScrambles = self.possibleScrambles(s1, s2)
        #print(allScrambles)
        if s2 in allScrambles:
            return True
        return False
        """
        return self.possibleScrambles2(s1, s2)

s = Solution()
print(s.isScramble("great","rgeat"))
print(s.isScramble("abcdefghijklmn","efghijklmncadb"))
print(s.isScramble("eebaacbcbcadaaedceaaacadccd","eadcaacabaddaceacbceaabeccd"))

"""
"abcdefghijklmn"
"efghijklmncadb"
"""