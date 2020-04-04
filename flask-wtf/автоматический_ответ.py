from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<string:text>')
@app.route('/index/<string:text>')
def index(text):
    return render_template('base.html', title=text)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    kwargs = {}
    kwargs['title'] = 'Анкета'
    kwargs['surname'] = 'Watny'
    kwargs['name'] = 'Mark'
    kwargs['education'] = 'выше среднего'
    kwargs['profession'] = 'штурман марсохода'
    kwargs['sex'] = 'male'
    kwargs['motivation'] = 'Всегда мечтал застрять на Марсе!'
    kwargs['ready'] = 'True'
    return render_template('auto_answer.html', **kwargs)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')