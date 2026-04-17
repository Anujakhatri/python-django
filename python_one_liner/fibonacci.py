# print fibonacci series up to 10 numbers
fibonacci = []
a, b = 0, 1
for i in range(10):
    fibonacci.append(a)
    a, b = b, a + b
print(fibonacci)


# using one-liner python codes
print([ (lambda x,f:f(x,f))(n, lambda n,f: n if n<=1 else f(n-1,f)+f(n-2,f)) for n in range(10)])
