from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json


pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/action_page.php',methods=['POST'])
def get_delay():

    result=request.form
    query_title = result['title']   #hERE, we created 3 variables
    query_author = result['author']
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_title, query_author, query_text)
    user_input = {'query':query}
    pred = pipeline.predict(query)
    print(pred)
    dic = {1:'Real',0:'Fake'}
    print(pred[0])
    return f'<html><body bgcolor="aqua"><h1 style="font-size:55px; margin-left: 1000px; font-family: monospace;">{dic[pred[0]]}</h1> <form action="/"> <button style="font-size:25px; margin-left: 1000px; font-family: courier;" type="submit">back </button> </form></body></html>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
