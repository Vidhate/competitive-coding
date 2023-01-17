# https://www.interviewbit.com/problems/power-of-two-integers/
def power(x, n, num):

    if n in [0,1]:
        return x

    x = power(x, int(n/2), num)
    x = x * x
    if n%2==1:
        x = x * num

    return x
    
def isPower(num):

    a, p = int(num**0.5)+1, 2
    while a>1:
        res = power(a, p, a)
        #print(a, p, res)
        if res>num:
            a-=1
        if res<num:
            p+=1
        if res==num:
            return True

    return False

print(isPower(int(input())))