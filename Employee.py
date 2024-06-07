class EmployeeDetails:
    def __init__(self,name, id, category,amount):
        self.name = name
        self.employee_ID = id
        self.category = category
        self.amount = amount
#instead of printing memory address we can add details to show in string
    def __repr__(self):
        return f"<Expense: {self.name},{self.employee_ID},{self.category},{self.amount: .2f}>"