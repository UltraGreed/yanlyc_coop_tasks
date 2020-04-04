from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from random import randint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.adress = 'module_1'
    user.email = 'scott_chief@mars.org'

    session.add(user)
    for i in range(3):
        user = User()
        user.surname = f"Colonist {str(i + 1)}"
        user.name = f'Colon {str(i + 1)}'
        user.age = randint(1, 100)
        user.position = f'looser {str(i + 1)}'
        user.speciality = 'research engineer {i + 1}'
        user.adress = f'module_{i + 1}'
        user.email = f'scotty_lover{str(i + 1)}@mars.org'
        session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()