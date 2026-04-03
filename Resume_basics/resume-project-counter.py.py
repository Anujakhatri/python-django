def project_counter(): 
    projects=int(input("How many projects are in your portfolio? "))

    for i in range(projects):
        projects = input("Enter project name: ")
        print("Project added:" + projects)
        
project_counter()        