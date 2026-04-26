# create a list of squares
squares=[]
for i in range(1,6):
    squares.append(i*i)
print(squares)

# using one-liner for list of squares
squares = [i*i for i in range(1,6)]
print(squares)

#using one-liner with condition of even numbers
evens=[]
evens = [i for i in range(10) if i%2==0]
print(evens)

#using one-liner with condition of odd numbers
odd=[]
odds= [i for i in range(10) if i%2!=0]
print(odds)

# flatten a 2D list
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = []
for sublist in lst:
    for item in sublist:
        flat.append(item)
print("Manual:", flat)

# using one-liner for flatten a 2D list
print("One-liner:", [item for sublist in lst for item in sublist])

# using itertools (the professional way)
import itertools
print("Itertools:", list(itertools.chain.from_iterable(lst)))

