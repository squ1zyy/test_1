class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return f"My name: {self.name}"

class User_2(User):
    def __init__(self, name, age, gender, job):
        super().__init__(self, name, age, gender)
        self.job = job


user1 = User('Alex', 12, "M")
print(user1.get_name())

user2 = User_2('Alex', 12, "M")
print(user2.get_name())