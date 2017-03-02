import os
import sqlite3
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
sys.path.append('../')
import demo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    if text=='':
	return render_template('form.html')
    else:
        with open('templates/answer.html', 'r+') as f:
	    f.seek(0)
	    f.write(demo.get_answer(text))
	    f.truncate()
       #return render_template('answer.html')
        return render_template('form.html', answer='answer.html', text = text)


if __name__ == "__main__":
    app.run()
