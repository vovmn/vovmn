

def f1(f):
    return f+4

def f2(n):
    return n**n

n = 10
f = f1(f2(n))
print(f)
n = 1
f = f1(f2(n))
print(f)