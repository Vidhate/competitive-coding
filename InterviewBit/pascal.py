A = int(input())

pascal = [[1],[1,1]]
for k in range(2,A):
    p = pascal[-1]
    row = [1] + [p[i]+p[i+1] for i,val in enumerate(p[:-1])] + [1]
    pascal.append(row)

return pascal[-1]