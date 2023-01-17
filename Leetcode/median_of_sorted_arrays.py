# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        k = m+n
        even = True if k%2==0 else False
        k = k//2
        track = 0
        A = []
        
        if m==0:
            if even:
                return (nums2[k]+nums2[k-1])/2
            else:
                return nums2[k]
            
        if n==0:
            if even:
                return (nums1[k]+nums1[k-1])/2
            else:
                return nums1[k]
            
        while track<=k:

            if not i<m:
                A.append(nums2[j])
                j+=1
            elif not j<n:
                A.append(nums1[i])
                i+=1
            elif nums1[i]<=nums2[j]:
                A.append(nums1[i])
                i+=1
            else:
                A.append(nums2[j])
                j+=1

            track+=1

        print(A)
        if not even:
            return A[k]
        else:
            return (A[k]+A[k-1])/2
            

s = Solution()
a = [1,2]
b = [3,4]
print(s.findMedianSortedArrays(a, b))