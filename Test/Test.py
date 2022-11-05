from flask import Flask, render_template,url_for
app = Flask(__name__)  # Flask 객체 생성
 
@app.route('/')
def index():
    return render_template('mainpage.html')
@app.route('/dc')
def dcPage():
    return render_template('DCpage.html')
@app.route('/dp')
def dpPage():
    return render_template('DPpage.html')
@app.route('/regist')
def registPage():
    return render_template('registPage.html')

# DP,DC 기능 추가
# DP 화면 추가

# 추후 C++로 만들어진 DP,DC 서버와 주고받는 파이썬 소켓 프로그래밍
# 헤더 - 데이터
# Test
if __name__ == "__main__":  # 모듈이 실행 됨을 알림
    app.run(debug=True, port=5000)  # 서버 실행, 파라미터로 debug 여부, port 설정 가능