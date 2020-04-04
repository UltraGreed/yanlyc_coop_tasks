from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index/<title>')
def index(title='Заготовка'):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('training.html', title='Инженерные тренажеры', img='/static/img/engineer.png')
    else:
        return render_template('training.html', title='Научные симуляторы', img='/static/img/science.png')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
