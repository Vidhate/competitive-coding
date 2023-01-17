def twoSum(nums, target):
    d = {}
    for i,num in enumerate(nums):
        rem = target-num
        if rem in d:
            return [d[rem], i]
        d[num] = i

    return

a, t = [int(x) for x in input().split()], int(input())
print(twoSum(a,t))