class Manager:
  
    def __init__(self, name, post, department, houseRent, transport):
     self.name = name
     self.post = post
     self.department = department
     self.basic = 50000 if self.department == "HR" else 25000
     self.houseRent = houseRent
     self.transport = transport


    def post_details(self):
        print("Name: " + self.name + "post is: " + self.post + "department is: " + self.department)

    def salary(self):
        calc_salary = self.basic + self.transport + self. houseRent
        print(calc_salary)


class Clerk:
    def __init__(self, name, post, houseRent, transport):
        self.name = name
        self.post = post
        self.houseRent = houseRent
        self.transport = transport
        self.basic = 15000


    def post_details(self):
        return "Name: " + self.name + "post is: " + self.post

    def salary(self):
        calc_salary = self.basic + self.transport + self. houseRent
        print(calc_salary)


Manone = Manager("Test", "trup", "HR", 2000, 200)
print(Manone.salary())
