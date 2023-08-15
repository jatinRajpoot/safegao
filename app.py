from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')
import csv
from datetime import datetime

@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/contactus')
def cart():
    return '''<h1>Phone No:- 7206382346</h1>
<h1>E-mail:- safegao172@gmail.com</h1>
'''

@app.route('/form')
def form():
    return render_template('Form.html')



@app.route('/contact', methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    brand = request.form['brand']
    website_type = request.form['website-type']
    name=str(name)
    email=str(email)
    phone=str(phone)
    brand=str(brand)
    website_type=str(website_type)
    with open("contact.csv","+a") as file:
        file.write(f"{name},{phone},{email},{website_type},{brand},{datetime.now()}\n")


    return render_template("Thankyou.html")

@app.route('/keytoadmin/<passw>')
def display_table(passw):
    if passw=="0":
        data = []
        with open('contact.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        return render_template('Admin.html', data=data)
    else:
        return "nikal bsdk"
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
app.run(host="0.0.0.0",debug=True)