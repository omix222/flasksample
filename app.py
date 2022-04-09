from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

# デコレータでURLマッピングする
@app.route('/next')
def hoge():
    return 'NextPage!!'

# render を使ってテンプレートファイルを利用
@app.route('/temp')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='flask test', name=name)

@app.route('/member')
def getmember():

    #db setting
    db = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )

    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    #return name
    return render_template('member.html', title='flask test', members=members) #変更

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')