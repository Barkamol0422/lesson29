class employee():
    def __init__(self,salary):
        self.salary=salary
        print(salary)
    def __del__(self):
        print("Your salary is deleted.")
a=employee(20000)
del a
