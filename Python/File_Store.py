employees = [["Ahmed Mohamed", "IT Engineer", 5000],
             ["Sameh Madbouly", "Sales Manager", 12000],
             ["Abdel Wahab Montaser", "Accountant",8000]]
# write employees to a file
""" f1 = open("Python\\emp_data.txt","w")
for emp in employees:
    f1.write("%-25s %-20s %-5d\n" %(emp[0],emp[1],emp[2]))
    
f1.close() """

# class employee to read data into it
class Employee:
    name = ""
    department = ""
    salary = 0

# read from file to class object
f2 = open("Python\\emp_data.txt","r")
for i in range(3):
    Employee.name = f2.read(26).strip()
    Employee.department=f2.read(21).strip()
    Employee.salary = f2.read(5).strip()
    print(Employee.name, " : ", Employee.department, " : ", Employee.salary)
    f2.__next__()
f2.close()

# another implementation to rad into class object
f2 = open("Python\\emp_data.txt","r")
lines = f2.readlines()
for line in lines:
    Employee.name = line[0:26].strip()
    Employee.department = line[26:47].strip()
    Employee.salary = line[47:53].strip()
    print(Employee.name, " : ", Employee.department, " : ", Employee.salary)
f2.close()