class Employee:
  def __init__(self, first, last, pay):
    self.first = first, 
    self.last = last,
    self.pay = pay

  def fullname(self, first, last):
    return self.first + " " + self.last

emp_1 = Employee("pablo", "raul", 60000)
print(emp_1, emp_1.fullname())
