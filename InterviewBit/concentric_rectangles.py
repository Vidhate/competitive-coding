def prettyPrint(A):
        
        res = []
        for i in range(A):
            row1, row2 = [], []
            base, j = A, 0
            while j<i:
                j+=1
                row1.append(base)
                row2 = [base] + row2
                base-=1

            while j<A:
                row1.append(base)
                row2 = [base] + row2
                j+=1

            res.append(row1+row2[1:])

        for i in range(2,A+1):
            res.append(res[A-i])

        for row in res:
            print(row)


prettyPrint(int(input()))