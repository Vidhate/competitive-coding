def solve(A,B):
    l, r, u, d = B-1, 8-B, A-1, 8-A
    q1, q2, q3, q4 = min(r,d), min(r,u), min(l,d), min(l,u)
    
    return q1+q2+q3+q4

def solve2(A, B, C):
    if A <= B-C+1:
        return C+A-1
    else:
        A-=(B-C+1)
        if A%B==0:
            return B
        else:
            return A%B

def maxSum(A, B):
    j = len(A)-1
    s=sum(A[:B])
    s_cur = s

    while B>0:
        s_cur += (A[j]-A[B-1])
        s = s_cur if s_cur>s else s
        B-=1
        j-=1

    return s

def findMinLights(A, B):

    lights, i = 0, 0
    while i<len(A):
        right_most = min(i+B-1,len(A)-1)
        while right_most-i>=0 and A[right_most]==0:
            right_most-=1

        if right_most-i==-1:
            return -1
        
        i = right_most + B
        lights+=1

    return lights

#print(solve2(int(input()), int(input()), int(input())))

#print(hammingDistance([int(x) for x in input().split()]))
#print(maxSum([int(x) for x in input().split()], int(input())))
#-533 -666 -500 169 724 478 358 -38 -536 705 -855 281 -173 961 -509 -5 942 -173 436 -609 -396 902 -847 -708 -618 421 -284 718 895 447 726 -229 538 869 912 667 -701 35 894 -297 811 322 -667 673 -336 141 711 -747 -132 547 644 -338 -243 -963 -141 -277 741 529 -222 -684 35

print(findMinLights([int(x) for x in input().split()], int(input())))




