# name = input ("Enter your name")
# Email= input ("Enter your email")
# Skills= input("Enter your skills")
# Experience = input ("Enter your Experience")


# Store employees in a list of dictionaries
employees = []
n=int(input("Enter number of employees: "))
for i in range(n):
    print(f"Enter details of employee {i+1}:")
    name= input ("Enter your name")
    salary = input ("Enter your salary")
    allowances = input ("Enter your allowances")
    deductions = input ("Enter your deductions")
    pan= input ("Enter your PAN number:")

    employee = {
        "name": name,
        "salary": salary,
        "allowances": allowances,
        "deductions": deductions,
        "pan": pan
    }
    employees.append(employee)

# Use tuples to define tax slabs:
tax_slabs = [
    (0, 500000, 0.01),
    (500000, 1000000, 0.10),
    (1000000, 2000000, 0.20),
    (2000000, float('inf'), 0.30)
]

#calculate tax based on slabs
def calculate_tax(salary):
    for slab in tax_slabs:
        if salary > slab[0] and salary <= slab[1]:
            tax = (salary - slab[0]) * slab[2]
            return tax
        
#use set to ensure unique PAN numbers
pan_numbers = set()
        
