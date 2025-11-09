from flask import Flask, Blueprint

app = Flask(__name__)
# Blueprint 객체 생성
# 첫 번째 인자는 블루프린트의 이름
# 두 번째 인자는 블루프린트가 정의되는 모듈의 이름으로 일반적으로 __name__
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
    return '로그인 페이지.'

@auth_blueprint.route('/logout')
def logout():
    return '로그아웃 페이지.'

app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)