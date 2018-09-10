# Priscilla Nunez
# SI 364
# 9/10/18


from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Task 2 : Dynamic URLS 
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
from flask import Flask
from flask import request
from flask import render_template
import requests
import json

app = Flask(__name__)
app.debug = True

## Routes
@app.route('/')
def root():
    return '<h1>✨Welcome✨</h1>'

## Problem 1
@app.route('/class/')
def _class():
    return '<h1>✨Welcome to SI 364!✨</h1>'

#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using POST method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body>
    <form method="GET" action = "http://127.0.0.1:5000/result">
    Ingredient :
    <input type"text" name"ingredient".</input> <ingredient : egg>
    <input type = "submit" name = "submit"></input>
    </form>
    </body>
    </html>
    '''
    return html_form

#Task 3.2 : Processing Form Data
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    if request.method == "GET": 
        ingg = request.args.get("ingredient")
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results 
    params = {}
    params["i"] = ingg
    response = requests.get("http://www.recipepuppy.com/api/", params = params)
    response_json = json.loads(response.text)
    response_str = str(response_json)
    return response_str


    #return "ingg"

# http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3 

if __name__ == '__main__':
    app.run(debug=True)
