#이론01: flask 로드하기. flask를 클래스 개념으로 생각하고 로드한다.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #루트 경로 이것은 루트 디렉토리

def index():
    return render_template("index.html")

@app.route('/register') #웹사이트의 디렉토리를 설정
def register():
    return "<h1>회원가입 페이지 입니다.<h1>"

@app.route('/board')
def board():
    return "<h1>게시판 목록 입니다.<h1>"

if __name__=="__main__":
    app.run()


