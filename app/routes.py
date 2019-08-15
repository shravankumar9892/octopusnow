# Original font: Ubuntu Mono
from app import app, mail
from flask import render_template, request, flash
from flask_mail import Message
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Index Page
@app.route('/')
def session():
    return render_template('index.html')

# Careers
@app.route('/careers')
def careers():
    return render_template('careers.html')
    
# Contact us
@app.route('/contactus', methods=['POST', 'GET'])
def contactus():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        text = request.form["text"]
        occupation = request.form["occupation"]
        mobile = request.form["mobile"]
        sheet = client.open_by_key('1_BzyI0SeTKeU8PpYR7NoUBtNmS2Qaoi1kY6qwWx3phM').sheet1
        row = [name, occupation, mobile, email, text]
        index = 1
        sheet.insert_row(row, index)
        msg = Message("Shravan from Octopus Now", sender="shravankumarshetty9892@gmail.com", recipients=[str(email)])
        msg.html = '''<h1>{name}!</h1>
<hr>
<p>Welcome {name}, I'm Shravan from Octopus Now and we're very happy to have you in our community. Being specialized in artificial intelligence we are constantly working to make human lives better.</p>

<h4>Are you a doctor or a data science enthusiast?</h4>
<p>We want to learn more about the people in our community, since you are the once we are working for everyday. We should know you well.</p>
<h5><i>Would you mind filling up this form? &#x21A0; <a href="">Community member details</a></i></h5>
<br>
<pre style="font-style:">
Regards,
<a href="tel:+919082514746">+919082514746</a>
<a href="mailto:shravankumarshetty9892@gmail.com">shravankumarshetty9892@gmail.com</a>
Shravan</pre>'''
        #with app.app_context():
        #    mail.send(msg)
        flash('Mail has been sent. Return to main page.')  
    return render_template('contactus.html')

# About us
@app.route('/aboutus')
def aboutus():
    return render_template('page.html')

@app.route('/in/octopusnow', methods=['GET', 'POST'])
def octopusnow():
    if request.method == 'POST':
        if list(request.form)[0] == 'search':
            question = request.form['search'] # From search bar
        else:
            question = list(request.form)[0]  # From Related questions
        data = {"question": question}
        #returnedanswer = requests.post(url="http://10ce91a8.ngrok.io/", json=data)
        #questions = returnedanswer.json()["octoreport"][0] # List of questions
        #answers = returnedanswer.json()["octoreport"][1] # List of answers
        answers = 'Unfortunately, there is no quick fix or cure for a cold. Get plenty of rest and fluids and give your body its best chance of fighting off the virus as fast as possible. You can take symptomatic relief to help you get back to your regular activities.'

        helpers = [('Safe Drug Bot','https://telegram.me/safedrugbot'), ('Izzy','https://www.messenger.com/t/izzyperiod'), ('Babylon Health','https://www.babylonhealth.com/'), ('Florence','https://florence.chat/'), ('Your.md','https://www.messenger.com/t/YourDotMD'), ('Ada','https://ada.com/'), ('Sensely','http://www.sensely.com/'), ('Buoy Health','https://www.buoyhealth.com/'), ('Infermedica','http://infermedica.com/'), ('Gyant','https://gyant.com/english/'), ('Bots4Health','https://bots4health.com/'), ('Cancer Chatbot','https://www.facebook.com/CancerChatbot/')]
        return render_template('octopusnow.html', answer=answers[0], question=question, helpers=helpers)#, relatedquestions=questions)


        # Uncomment below code to test without activating colab server.
        #answer = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam rutrum metus non elit vehicula pellentesque. Mauris ac metus eu mauris vestibulum consectetur. Morbi feugiat nunc id arcu varius, a congue lectus congue. Nulla felis dolor, posuere et hendrerit ac, pretium sed mi. Vivamus ligula urna, accumsan non lorem ac, commodo efficitur eros. Sed eget purus orci. Nulla vulputate nulla vel sem facilisis, et facilisis sem iaculis.'
        #relatedquestions = ['what is answer to question 1?', 'what is answer to question 1?', 'what is answer to question 1?', 'what is answer to question 1?']
        #return render_template('octopusnow.html', answer=answer, question=request.form["search"], helpers=helpers, relatedquestions=relatedquestions)


    if request.method == 'GET':
        if extras:
            question = extras
            data = {"question": question}
            returnedanswer = requests.post(url="http://10ce91a8.ngrok.io/", json=data)
            print(returnedanswer)
            helpers = [('+919769253823', 'Shravan'), ('+919869195954', 'Vishala'), ('02224931781', 'Home')]
            #questions = returnedanswer.json()["octoreport"][0]
            #answers = returnedanswer.json()["octoreport"][1]
            return render_template('octopusnow.html', answer=returnedanswer, helpers=helpers)
        else:
            question='Ask now...'
            return render_template('octopusnow.html', question=question)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index404.html')

@app.errorhandler(405)
def method_not_found(e):
    return render_template('index405.html')

@app.errorhandler(500)
def _not_found(e):
    return render_template('index500.html')
