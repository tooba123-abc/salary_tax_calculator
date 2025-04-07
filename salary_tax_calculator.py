print("Welcome To Salary Tax Calculator")
print("lets calculate your monthly and yearly tax")
print("--------------------------------\n")

# Step 1: Take user input
name=input("enter your name:")
designation= input("enter your job title:")
monthly_salary= float(input("Enter Your Monthly Salary (PKR):"))


# Step 2: Show user input summary
print("/n Summary Of Your Info")
print(f" Name :{name}")
print(f" Job Title: {designation}")
print(f" Month Salary: Rs .{monthly_salary:,.2f}")


# Step 3: Calculate yearly salary
yearly_salary = monthly_salary * 12



# Step 4: Decide tax rate based on monthly salary

if monthly_salary <= 50000:
    tax_rate = 0
   
elif monthly_salary <=100000:
   tax_rate = 5 
    
elif monthly_salary <=200000:
    tax_rate = 10

elif monthly_salary <= 500000:
    tax_rate = 15

else:
    tax_rate = 20


# Step 5: Calculate monthly and yearly tax
monthly_tax = (monthly_salary * tax_rate) / 100
yearly_tax = monthly_tax * 12

# Step 6: calculate monthly and yearly net
monthly_net = monthly_salary - monthly_tax
yearly_net = yearly_salary - yearly_tax 

# Step 7: Display full breakdown
print("\n Tax Breakdown:")
print(f"applicable monthly tax rate : {tax_rate}%")
print(f" monthly_tax: Rs.{monthly_tax# Step 7: Display full breakdown
print("\n Tax Breakdown:")
print(f"applicable monthly tax rate : {tax_rate}%")
print(f" monthly_tax: Rs.{monthly_tax:,.2f}")
print(f" yearly_tax: Rs.{yearly_tax:,.2f}")

print("\n final salary after tax")
print(f" monthly_salary: Rs.{monthly_net:,.2f}")
print(f" yearly_salary: Rs.{yearly_net:,.2f}")


# step 8 : feedback message
if tax_rate == 0:
    print("\n great! you are in no tax bracket.")
elif tax_rate <=10:
    print("\n moderate tax ! plan your saving wisely")
else:
    print("\n high tax detected! consider investment options to save tax")
