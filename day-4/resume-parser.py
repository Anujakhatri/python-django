# name = input ("Enter your name")
# Email= input ("Enter your email")
# Skills= input("Enter your skills")
# Experience = input ("Enter your Experience")


# Store employees in a list of dictionaries
employees = []
n=int(input(" Enter number of employees: "))
for i in range(n):
    print(f" Enter details of employee {i+1}:")
    name= input (" Enter your name")
    salary = input (" Enter your salary")
    allowances = input (" Enter your allowances")
    deductions = input (" Enter your deductions")
    pan= input (" Enter your PAN number:")

    employee = {
        "name": name,
        "salary": salary,
        "allowances": allowances,
        "deductions": deductions,
        "pan": pan
    }
    employees.append(employee)

# Use tuples to define tax slabs:
# tax_slabs = [
#     (0, 500000, 0.01),
#     (500000, 1000000, 0.10),
#     (1000000, 2000000, 0.20),
#     (2000000, float('inf'), 0.30)
# ]

#calculate tax based on slabs
def calculate_tax(salary):
    tax_slabs = [
        (0, 500000, 0.01),            #slab 1
        (500000, 1000000, 0.10),      #slab 2
        (1000000, 2000000, 0.20),     #slab 3
        (2000000, float('inf'), 0.30) #slab 4
    ]
    #invalid salary check
    if salary <=0:
        return 0
    
    total_tax =0
    seperate =[]
    
    #loop through tax slabs
    
    for slab in tax_slabs:
        #tuple unpacking
        lower, upper, rate = slab
        
        #check if salary is less than or equal to lower bound
        #if salary = 50,000 stops at slab 2 because 50,00 <= 50,000
        if salary<=lower:
            break
        
        taxable_amount = min(salary, upper) - lower #get only amount that belongs to this slab
        tax_in_slab = taxable_amount * rate
        total_tax += tax_in_slab
        seperate.append((lower, upper, rate,taxable_amount, tax_in_slab))  
               
    return total_tax, seperate  
        
#use set to ensure unique PAN numbers
def generate_tax_report(name, pan , salary):
    total_tax , seperate = calculate_tax(salary)
    report = f"""
            ====================================
                TAX REPORT
        ====================================
        Name        : {name}
        PAN         : {pan}
        Gross Salary: Rs.{salary:,.2f}
        ------------------------------------
        SLAB SEPERATION
        ------------------------------------ """
        
    for lower, upper, rate, taxable_amount, tax_in_slab in seperate:
        upper_display = f"Rs.{upper:,.0f}" if upper != float('inf') else "INFINITY"
        report += f"""
        SLAB RS{lower:,.0f} to {upper_display}
        Rate : {rate *100:,.0f}%
        Taxable Amount : Rs.{taxable_amount:,.2f}
        Tax : Rs.{tax_in_slab:,.2f}
        """
    report += f"""
        ------------------------------------
        Total Tax : Rs.{total_tax:,.2f}
        Net Salary : Rs.{salary - total_tax:,.2f}
        ===================================="""
        
    return report

pan_numbers = set()

for employee in employees:
    name = employee["name"]
    pan = employee["pan"]
    salary = (employee["salary"])
    
    #dublicate PAN check
    if pan in pan_numbers:
        print(f"Duplicate PAN number found: {pan} ({name})")
        continue
    
    pan_numbers.add(pan)
    print(report = generate_tax_report(name, pan,salary))
        
