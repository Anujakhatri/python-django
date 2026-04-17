
x= 10

if x > 5:
    print("Greater than 5")
else:
    print("Less or equal to 5")

# Using ternary operator (one-liner)
print("Greater than 5") if x > 5 else print("Less or equal to 5")

# condition check
result="Yes" if x>10 else "No"
print(result)

# check all element is unique
listt=[1,2,3,1,4,2,4,5,6,7,3,4]
print("Unique") if len(set(listt))== len(listt) else print("Not Unique")

# check if two lists are anagrams
s1, s2 = "earth", "heart"
s3, s4 = "python", "java"
print("Anagrams") if sorted(s1)==sorted(s2) else print("Not Anagrams")
print("Anagrams") if sorted(s3)==sorted(s4) else print("Not Anagrams")

#  Check if all elements in the list are true
l1, l2 = [True, True, True], [True, True, False]
print("All True") if all(l1) else print("Not all True")
print("All True") if all(l2) else print("Not all True")



