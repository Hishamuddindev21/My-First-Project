

employee_file =open("emplyee.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

