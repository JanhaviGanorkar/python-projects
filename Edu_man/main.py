class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

    def __str__(self):
        return self.get_details()

class Staff(Person):
    def __init__(self, name, age, address, staff_id, role, working_hours):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.role = role
        self.working_hours = working_hours

    def monthly_hours(self):
        return self.working_hours * 30

    def __str__(self):
        return f"{super().__str__()}, Staff ID: {self.staff_id}, Role: {self.role}, Monthly Hours: {self.monthly_hours()}"

obj = Staff("janhavi", "22", "amravati", 1, "teacher", 3)
print(obj)