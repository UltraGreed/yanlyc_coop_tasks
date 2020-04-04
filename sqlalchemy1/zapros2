name = input()
global_init(name)
session = create_session()
for user in session.query(User).filter(User.address == "module_1",
                                       User.position.notlike('%ingeneer%'),
                                       User.speciality.notlike('%ingeneer%')):
    print(user)
