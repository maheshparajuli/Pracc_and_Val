class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline().strip()
            salary = int(f.readline().strip())
        return cls(name, salary)

e1=Employee.from_file("employee.txt")
print(e1.name)