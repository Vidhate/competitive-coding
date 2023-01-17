# https://www.interviewbit.com/problems/square-root-of-integer/
def sqrt(A):
    mn, mx = 1, A
    if A in [0, 1]:
        return A

    mid = (mn+mx)//2
    while mn<=mx:
        mid = (mn+mx)//2
        s1, s2 = mid*mid, (mid+1)*(mid+1)
        print(mid, s1, s2)
        if s1<=A and s2>A:
            return mid
        elif s1<A:
            mn = mid+1
        else:
            mx = mid-1

    return mid

print(sqrt(int(input())))