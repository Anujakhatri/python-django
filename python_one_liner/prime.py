# print prime numbers between 1 to 50
primes = []
for i in range(2,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        primes.append(i)
print(primes)        

# using python one liner code
print([x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))])
