def solution(n):
    solution =[]
    while (n // 1000 >= 1):
        solution.append("M")
        n = n - 1000
    while (n // 500 >= 1):
        if (n >= 900):
            solution.append("CM")
            n = n - 900
            break
        solution.append("D")
        n = n - 500
    while (n // 100 >= 1):
        if (n >= 400):
            solution.append("CD")
            n = n - 400
            break
        solution.append("C")
        n = n - 100
    while (n // 50 >= 1):
        if (n >= 90):
            solution.append("XC")
            n = n - 90
            break
        solution.append("L")
        n = n - 50
    while (n // 10 >= 1):
        if (n >= 40):
            solution.append("XL")
            n = n - 40
            break
        solution.append("X")
        n = n - 10
    while (n // 5 >= 1):
        if (n == 9):
            solution.append("IX")
            n = n - 9
            break
        solution.append("V")
        n = n - 5
    while (n // 1 >= 1):
        if (n == 4):
            solution.append("IV")
            break
        solution.append("I")
        n = n - 1
    return "".join(solution)

print(solution(92))

"""
"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1
 
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""