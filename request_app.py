from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '홈페이지'

# 요청 처리
@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"

# 응답 처리
@app.route('/json')
def json_example():
    # jsonify를 이용하여 JSON형식의 응답 반환
    return jsonify({"message": "Hello, World!"})
    # jsonify를 사용하는 이유
    # MIME 타입 설정: 응답 헤더에 Content-Type:application/json을 설정하여 응답이 JSON형식임을 명시한다.
    # 특수 문자 처리: 파이썬의 딕셔너리에 포함된 특수문자를 JSON표준에 맞게 이스케이프 처리한다.
    # 유니코드 지원: 유니코드 문자를 오랍르게 처리하고 응답을 UTF-8로 인코딩하여 반환한다.

@app.route('/response')
def response_example():
    # 응답 객체 생성. make_response(응답 바디, 상태 코드)
    resp = make_response("Hello with header", 200)
    
    # Custom-Header 라는 이름의 사용자 정의 헤더를 설정하고 custom-value 값을 지정
    resp.headers['Custom-Header'] = 'Custom-value'
    # 설정한 헤더와 함께 응답 객체 반환
    return resp