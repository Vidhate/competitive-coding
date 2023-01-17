# https://www.interviewbit.com/problems/excel-column-title/
def convertToTitle(A):
    d = {
        1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O', 16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S',
        20 : 'T', 21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y', 0 : 'Z'
    }
    s = ""
    while A>0:

        dig = d[A%26]
        s = dig + s
        print(A%26, int(A/26), dig, s)

        A = int(A/26) - 1 if A%26==0 else int(A/26)


    return s

print(convertToTitle(int(input())))