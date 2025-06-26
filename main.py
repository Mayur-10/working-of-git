# flask app
from flask import Flask

app = Flask(__name__)  ### WSGI app

@app.route('/') # API # Default API
def one():
    return "flask api"

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True)