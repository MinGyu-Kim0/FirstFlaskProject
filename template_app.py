from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '홈페이지'

@app.route('/hello/<name>')
def hello_name(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template('hello.html', name=name, timestamp=now)

@app.route('/fruits')
def show_fruits():
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    return render_template('fruits_list.html', fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)