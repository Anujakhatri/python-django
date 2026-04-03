#resume eligibility check
def resume_eligibility(): 
    name=input("Enter your name: ")
    experience = int(input("How many years of experience: ")) 

    if experience>=5:
        print(name + " eligible for lead developer")
        
    else:
        print(name + " eligible for junior developer")

resume_eligibility()