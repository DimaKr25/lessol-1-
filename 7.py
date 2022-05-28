class Step:
    def __init__(self,name = "name", age = 0):
        self.userName = name
        self.age = age
    def get_name(self):
        return self.userName
    def set_name(self, name):
        self.userName = name
user = Step()
# print(user.serName)
print(user.get_name())
user.set_name("Jony")
print(user.get_name())