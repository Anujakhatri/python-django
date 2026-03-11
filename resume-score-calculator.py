score =0
python = int(input("how much python do you know? (export/begineer): "))
java = int(input("how much java do you know?: (export/begineer): "))
c = int(input("how much c do you know? (export/begineer): "))

if python == "export":
    python = score + 10
if java == "export": 
    java = score + 10
if c == "export":
    c = score + 10   

print("your resume score is: " + score)