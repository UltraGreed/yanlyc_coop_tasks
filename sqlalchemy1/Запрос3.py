name = input()
global_init(name)
session = create_session()
for user in session.query(User).filter(User.age < 18):
    print(user, user.age, 'years')