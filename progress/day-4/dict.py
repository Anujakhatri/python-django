#dictionary
intro= {
    "name": "anuja", "age": 24, "city": "kathmandu"
}
print(intro['name'])

#add element in python
intro["profession"]="student"
print(intro.get("profession"))

del intro["city"]
print(intro)
print(intro.pop("profession"))

#loop
for key in intro:
    print(key,intro[key])
    
for key, value in intro.items():
    print(key, value)

#.keys() .values() .items()
#get() method
#update() method
#clear() method    
    
    
