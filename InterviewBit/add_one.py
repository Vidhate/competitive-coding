# https://www.interviewbit.com/problems/add-one-to-number/
def plusOne(A):
    carry = 0
    num = []
    j = len(A)-2
    dig, carry = (A[-1]+1)%10, int((A[-1]+1)/10)
    num = [dig] + num

    while j>=0:
        dig, carry = (A[j]+carry)%10, int((A[j]+carry)/10)
        num = [dig] + num
        j-=1

    while carry>0:
        num = [carry%10] + num
        carry = int(carry/10)

    i = 0
    while num[i]==0:
        i+=1

    return num[i:]

print(plusOne([int(x) for x in input().split()]))