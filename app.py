from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'
# デコレータでURLマッピングする
@app.route('/next')
def hoge():
    return 'NextPage!!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')