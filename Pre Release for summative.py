#Task 1
best_emp_name=0
best_emp=0
p=0
hpay=0
pay1=0
pay2=0
pay3=0
pay4=0
pay5=0

for i in range (1,31):
    emp_name = input("Enter Your Name: ")
    emp_num = int(input("Enter Number: "))
    hrs = int(input("Enter Number of hours worked: "))

#Task 2
    if hrs < 5:
        p=0
        pay1 = pay1 + 1

    elif hrs >= 5 and hrs <= 9:
        p=70
        pay2 = pay2 + 1

    elif hrs >=10 and hrs <= 14:
        p=100
        pay3 = pay3 + 1

    elif hrs >= 15 and hrs <= 18:
        p=150
        pay4 = pay4 + 1

    elif hrs >=19:
        p=200
        pay5 = pay5 + 1

    hr_pay = hrs * p
    print("Your Pay :", hr_pay)

    if hpay < hrs:
        hpay = hrs
        best_emp_name = emp_name
        best_emp_num = emp_num
        best_emp_pay = hr_pay * 1.2

print("Best employee is,", best_emp_name)
print("Best Employee number is,", best_emp_num)
print("New Pay for Best Employee is,", best_emp_pay)

#Task 3
print("Total Number of Employees who work less thn 5 hours-", pay1)
print("Total Number of Employees who work between 5 and 9 hours-", pay2)
print("Total Number of Employees who work between 10 and 14 hours-", pay3)
print("Total Number of Employees who work between 15 and 18 hours-", pay4)
print("Total Number of Employees who work more than 19 hours-", pay5)
