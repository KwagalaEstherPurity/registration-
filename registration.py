class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number
    
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")


student1 = Student("Esther Purity", "S23B13/026")
student1.display_info()

student2 = Student("Shilla Ralph", "S23D13/001")
student2.display_info()
