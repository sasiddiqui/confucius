import os
import sqlite3
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
sys.path.append('../')
import demo
import glob

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
        if os.path.exists("templates/temp/"):
            for CleanUp in glob.glob("templates/temp/*.*"):
                os.remove(CleanUp)
                                   
        qname = text.replace(' ','_')
#	with open('templates/answer.html', 'r+') as f:
#	    f.seek(0)
#	    f.write(demo.get_answer(text, '90e7acx197-nlc-170').encode('utf-8'))
#	    f.truncate()
        with open('templates/temp/'+qname+'.html', 'w+') as f:
            f.seek(0)
            f.write('<br/><p>Retrieve data:</p><br/>')
            f.write(demo.get_retrieve(text, '90e7acx197-nlc-170').encode('utf-8'))
            f.write('<br/><p>Rank data:</p><br/>')
	    f.write(demo.get_rank(text, '90e7acx197-nlc-170').encode('utf-8'))
            f.truncate()
        return render_template('form.html', answer='temp/'+qname+'.html', text = demo.get_rank(text, '90e7acx197-nlc-170'))


if __name__ == "__main__":
    extra_files = ['templates/answer.html',]
    app.run(extra_files=extra_files)
