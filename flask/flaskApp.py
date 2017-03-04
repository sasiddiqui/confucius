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
        return render_template('form.html', answer=demo.get_answer(text), text = text)


if __name__ == "__main__":
    extra_files = ['templates/answer.html',]
    app.run(extra_files=extra_files)
