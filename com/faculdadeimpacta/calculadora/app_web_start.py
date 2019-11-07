from flask import Flask


app = Flask(__name__)


app.run(host='0.0.0.0')
@app.route('/devops_ac8')
def index():
    return 'Boa noite!, Passei direto'


if __name__ == '__main__':
    app.run()
