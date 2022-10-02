def factorial(a):
    f = []
    tmp = 1
    for i in range(1, a + 1):
        tmp *= i
        f.append(tmp)
    return f

n = int(input())

print(factorial(n))
