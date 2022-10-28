from datetime import date, datetime
from email import message, message_from_binary_file
import email
from fileinput import filename
from pydoc import render_doc
from token import NEWLINE
from unicodedata import name
from flask import Flask, render_template, url_for, request
import re
import csv
from flask import request

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",
    name=name,
    date=datetime.now())

@app.route('/Contacts.html')
def about():
    return render_template('Contacts.html')

@app.route('/blog')
def blog():
    return 'This is just an example'
    
@app.route('/blog/2020/dogs')
def blog2():
    return 'But it is fun'

@app.route("/hello/<name>")
def xhello_there(name):
    now = datetime.now()
    formatted_now =now.strftime("%A, %d %B, %Y at %X")

def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a')as database:
        email = data ["email"]
        subject = data ["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data ["subject"]
        message = data["message"]
        csv_write =  csv.writer(database2 ,delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
       if request.method == 'POST':
        try:
         data = request.form.to_dict()
         write_to_csv(data)
         return 'Message sent'
        except:
            return 'data not sent to database'
       else:
        return 'Not sent'
