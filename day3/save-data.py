def saveDataToFile():
    file = open("userdata.txt", "a")
    for i in range(3):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        
        #writing to the file
        file.write(f"Name: {name}, Age: {age} \n")

    file.close()
    
saveDataToFile()

def readDataFromFile():
    file = open("userdata.txt", "r")
    data = file.read()
    print( "User Data: \n", data)
    file.close()

readDataFromFile()