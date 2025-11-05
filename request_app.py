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

    # header는 HTTP 요청과 응답 메시지의 일부로, 클라이언트와 서버 간의 통신에 대한 추가적인 정보를 제공한다.

@app.route('/response')
def response_example():
    # 응답 객체 생성. make_response(응답 바디, 상태 코드)
    resp = make_response("Hello with header", 200)
    
    # Custom-Header 라는 이름의 사용자 정의 헤더를 설정하고 custom-value 값을 지정
    resp.headers['Custom-Header'] = 'Custom-value'
    # 설정한 헤더와 함께 응답 객체 반환
    return resp

# make_response() 함수 호출 시 세 번째 인자로 headers를 직접 딕셔너리 형태로 넘겨주는 방법
# 생성 시점에 모든 정보를 한 번에 넘길 때 좋음
@app.route('/direct')
def direct_response():
    headers = {'X-Example': 'DirectHeader'}
    return make_response("Direct Response", 200, headers)

# make_response()를 호출하여 생성된 응답 객체에 .headers 속성을 사용하여 헤더를 추가하는 방법
# 응답 객체를 조금 더 유동적으로 다룰 필요가 있을 때 좋음
@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 202)
    response.headers['X-Example'] = 'CustomHeader'
    return response