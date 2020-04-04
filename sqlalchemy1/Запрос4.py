name = input()
global_init(name)
session = create_session()
for user in session.query(User).filter(User.position.like("%chief%") | User.position.like("%middle%")):
    print(user, user.position)