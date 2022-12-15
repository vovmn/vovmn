def f1(n):
    def f2(m):
        return n+m
    return f2


n = 10
m = 15
print(f1(n)(m))