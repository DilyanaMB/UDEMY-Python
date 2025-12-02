class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

user1 = User('001', 'Deya')
user3 = User ('003','Victor')
user1.follow(user3)
print(user1.followers)
print(user1.following)
print(user3.followers)
print(user3.following)

def function():
    pass  # do nothing, just allows to have class, func etc that is empty

print("hello")

class UserWithEmptyConstructor:
    pass

user2 = UserWithEmptyConstructor()
user2.id = '002'  # adding attributes to class's object

print(user2.id)
