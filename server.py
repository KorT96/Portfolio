from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(f'{page_name}')

def write_file(data):
    with open('database.txt', mode='a',) as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        new_file = database.write(f'\n{email} , {subject} , {message}')

def write_csv(data):
    with open('database.csv', mode='a',  newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data= request.form.to_dict()
            write_csv(data)
            return redirect('thankyou.html')
        else:
            print('Something is wrong somewhere')
    except:
        return ('Didn\'t get saved to database')        
    finally:
        print('All done')