from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about_page():
    # 'render_template' 함수를 사용하여 'about.html' 템플릿을 렌더링합니다.
    # 플라스크는 'about.html'과 함게 이 템플릿이 상속하는 모든 부모 템플릿을 렌더링하여 최종 HTML생성
    return render_template('about.html')