from api_site import add_result , get_results
from time import sleep

from flask import Flask, render_template , request , redirect
app = Flask(__name__)



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
            add_result(first_num,second_num,action)
        except:
            return 'error'
        return redirect('/')

@app.route('/calc')
def calc():
    all_results = get_results()
    return render_template('db.html',rows=all_results)
if __name__ == '__main__':
    app.run(debug=True)
 