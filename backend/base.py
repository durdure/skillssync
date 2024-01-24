from flask import Flask

app = Flask(__name__)

@app.route('/')
def fine():
    return True

if __name__ == '__main__':
    app.run(port='0.0.0.0', debug=True)