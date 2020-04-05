name = input()
global_init(name)
session = create_session()
biggest = 0
teams = set()
for user in session.query(User).filter(User.address == 'module_1', User.age < 21):
    user.address = 'module_3'