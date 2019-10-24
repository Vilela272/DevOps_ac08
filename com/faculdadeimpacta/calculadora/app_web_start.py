from flask import Flask


app = Flask(__name__)


@app.route('/devops_ac8')
def index():
    return 'Index Page!'


if __name__ == '__main__':
    app.run()
