from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/charts')
def render_charts():  # put application's code'
    return render_template('charts.html')


@app.route('/tables')
def render_tables():  # put application's code'
    return render_template('tables.html')


if __name__ == '__main__':
    app.run()
