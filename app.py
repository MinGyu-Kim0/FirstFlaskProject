from flask import Flask, url_for
app = Flask(__name__)

# 뷰 함수 : 사용자 프로필을 보여줍니다.
@app.route('/user/<username>')
def show_user_profile(username):
    # 실제로는 프로필 페이지를 보여주는 로직이 위치
    return f'User {username}'

# 뷰 함수 : 게시물을 보여줍니다.
@app.route('/post/<year>/<month>/<day>')
def show_post(year, month, day):
    # 실제로는 게시물 페이지를 보여주는 로직이 위치
    return f'Post for {year}/{month}/{day}'

# 홈페이지에서 url_for를 이용하여 위의 뷰 함수들로 이동하는 링크를 생성
@app.route('/')
def index():
    # show_user_profile 뷰로 이동하는 URL 생성
    user_url = url_for('show_user_profile', username='mingyu')
   
    # show_post 뷰로 이동하는 URL을 생성합니다.
    post_url = url_for('show_post', year='2025', month='11', day='03')
   
    # 생성된 URL 반환
    return f'User URL: {user_url}<br>Post URL: {post_url}'

if __name__ == '__main__':
    app.run(debug=True)
