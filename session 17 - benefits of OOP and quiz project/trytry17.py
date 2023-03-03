# traditional way to add atribute in class
print('>>> traditional way')
class User:
    pass

user_1 = User()
user_1.id = '01'
user_1.username = 'jojo'
print(user_1.id)

user_2 = User()
user_2.id = '02'
user_2.username = 'jeje'
print(user_2.username)

# with class
print('>>> with class')
class User2():
    def __init__(self, id, username,):
        self.user_id = id
        self.user_name = username
        self.followers = 0

# simpler, with just one line vs 3 lines
user_11 = User2('01', 'juju')
user_22 = User2('02', 'jaja')
print(user_11.user_id)
print(user_22.user_name)


print('>>> with method')
class User3():
    def __init__(self, id, username,):
        self.user_id = id
        self.user_name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # method has a self parameter
        self.following += 1
        user.followers += 1

user_111 = User3('1', 'lulu')
user_222 = User3('2', 'lala')

user_111.follow(user_222)
print(f"user 111 following: {user_111.following}")
print(f"user 111 followers: {user_111.followers}")
print(f"user 222 followers: {user_222.followers}")
print(f"user 222 before following: {user_222.following}")

user_222.follow(user_111)
print(f"user 222 after following: {user_222.following}")
