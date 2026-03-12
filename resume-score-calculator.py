score =0
def resume_score():
    
    python = input("how much python do you know? (export/begineer): ")
    java = input("how much java do you know?: (export/begineer): ")
    c = input("how much c do you know? (export/begineer): ")

    if python == "export":
        python = score + 10
    if java == "export": 
        java = score + 10
    if c == "export":
        c = score + 10   

    print("your resume score is: " + str(score))
    
resume_score()   