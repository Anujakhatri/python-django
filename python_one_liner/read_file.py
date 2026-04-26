
data=open("data.txt","r")
print(data.read())

# using one-liner to read a file
with open("data.txt","r") as f:
    print(f.read())