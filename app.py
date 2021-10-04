from flask import Flask
from oauth import kakao, naver, google

app = Flask(__name__)

app.register_blueprint(kakao.bp)
app.register_blueprint(naver.bp)
app.register_blueprint(google.bp)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
