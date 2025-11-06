from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# static : 정적 파일이 저장되는 폴더. 이미지, 자바스크립트, CSS파일 등을 이곳에 저장한다.
# templates : HTML템플릿 파일이 저장되는 폴더. 플라스크는 Jinja2 템플릿 엔진을 사용해 HTML을 렌더링한다.
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image')
def get_image():
    return send_from_directory(app.static_folder, 'image.jpg')