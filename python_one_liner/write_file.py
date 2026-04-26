data="Hello World"
with open("test.txt","w") as f:
    f.write(data)

# using one-liner to write a file
open("data.txt", "w").write("Hello World")
