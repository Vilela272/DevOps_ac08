from flask import Flask


app = Flask(__name__)


app.run(host='0.0.0.0')
@app.route('/devops_ac8')
def index():
    return 'Index Page!'


if __name__ == '__main__':
    app.run()
