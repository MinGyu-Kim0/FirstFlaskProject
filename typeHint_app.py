from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '홈페이지'

@app.route('/int/<int:var>')
def int_type(var: int):
    return f'Interger: {var}'

@app.route('/float/<float:var>')
def float_type(var: float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'
