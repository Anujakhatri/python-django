#data strucuture in python
#list
mylist = [1,2.98,3,4,"python",True]
#accessing list 
print(mylist[0])
#add element in list
mylist.append("coderush")   
print(mylist)
#insert element in list 
mylist.insert(2,"programming")
print(mylist)
#remove element from list
mylist.remove(2.98)
print(mylist)

#loop through list
for item in mylist:
    print(item)

#tuple immutable list
gpsValues = (27.1212, 85.3232)
print(gpsValues[0])

#dictionary
intro = {"name":"anuja", "age": 24, "city": "butwal"}
print(intro["name"])
#add element in dictionary
intro["profession"] = "student"
#sequence of characters
name = "anuja"
city = "Butwal"
print(name[0])
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title()) # len()