def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo2(n):
    a, b = 0, 1
    while n>0:
        a, b = b, a + b
        n -=1
    return a

n = int(input())

# print(fibo(n))
print(fibo2(n))

