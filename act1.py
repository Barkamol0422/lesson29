class IOString():
    def __init__(self):
        self.str1=""
    def string(self):
        self.str1=input("Enter a string: ")
    def output(self):
        print("Upper case of the string, ",self.str1.upper())
str1=IOString()
str1.string()
str1.output()
