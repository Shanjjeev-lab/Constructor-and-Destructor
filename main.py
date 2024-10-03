class Employee:

    def __init__(self):
        print("Employee is created!")

    def __del__(self):
        print("Employee is deleted")

employee1 = Employee()
del employee1
