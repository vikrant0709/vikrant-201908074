from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Running CST FLASK DOCKER..."

@app.route('/check2', methods=["GET"])
def index():
    return "Running Check2..."