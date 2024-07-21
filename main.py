import sqlite3
from time import sleep

from flask import Flask, render_template , request , redirect
app = Flask(__name__)

db = sqlite3.connect('calc.db',check_same_thread=False)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        sleep(5)
        first_num = request.form.get('first_num')
        second_num = request.form.get('second_num')
        action = request.form.get('action')
        try:
            res = eval(first_num+action+second_num)
        except:
            res = 'Ошибка ввода!'
        cursor.execute("INSERT INTO calc VALUES (?,?,?,?)",(first_num,second_num,action,res))
        db.commit()
        return redirect('/')

@app.route('/calc')
def calc():
    rows = cursor.execute("SELECT * FROM calc").fetchall() 
    return render_template('db.html', rows=rows)
if __name__ == '__main__':
    app.run(debug=True)
 