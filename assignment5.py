from flask import Flask, render_template, request, escape, render_template
import os

app = Flask(__name__)

class question:
    def __init__(self, qtitle, qtext, qanswer):
        self.title = qtitle
        self.text = qtext
        self.answer = qanswer 

test = {}

@app.route('/', methods = ['GET','POST'])
def submit ():
    if request.method == 'GET':
        return app.send_static_file('enter.html')

    else:
        test[escape(request.form['title'])] = question(escape(request.form['title']), escape(request.form['question']), escape(request.form['answer']))
        return app.send_static_file('complete.html')

@app.route('/answer', methods = ['GET','POST'])
def trivia():
    if request.method == 'GET':
        return render_template('test.html', titles = test.keys(), questions = test.values());
    
    else:
        if escape(request.form['answer']).upper() == test[escape(request.form['title'])].answer.upper():
            return app.send_static_file('correct.html')
        else:
            return render_template('wrong.html', answer = test[escape(request.form['title'])].answer, question = test[escape(request.form['title'])].text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port)