def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
c=factorial(998)
# d=str(c)
print(c)
# print(len(d))
