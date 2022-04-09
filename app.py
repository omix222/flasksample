from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'
# デコレータでURLマッピングする
@app.route('/next')
def hoge():
    return 'NextPage!!'
@app.route('/temp')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='flask test', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')