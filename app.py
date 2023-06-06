from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hi, here. This is the demo of our project. access: 127.0.0.1:8888/bar'


@app.route('/bar')
def get_bar():
    return render_template("demo.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
