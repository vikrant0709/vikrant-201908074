from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Running CST FLASK DOCKER..."

@app.route('/check2', methods=["GET"])
def check2():
    return "Running Check2..."

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
