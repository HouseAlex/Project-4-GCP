from flask import Flask, render_template, redirect, url_for, g, request
import os

app = Flask(__name__)

user_data = {}

creatorFirst = 'Alex'
creatorLast = 'House'
creatorEmail = 'AlexTest@gmail.com'

@app.route('/chat', methods=['GET'])
def chat():
    return render_template('chat.html')

@app.route('/', methods=['GET'])
def loadPrompt():
    return render_template('info-entry.html')

@app.route('/info-entry', methods=['POST'])
def infoEntry():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        user_data['first_name'] = firstname
        user_data['last_name'] = lastname
        user_data['email'] = email

        return redirect(url_for('chat'))

@app.route('/question/<int:questionId>', methods=['GET'])
def questionSelected(questionId):
    response = handle_message(questionId)
    return {'fulfillmentText': response}

@app.route('/quit', methods=['GET'])
def quit():

    return render_template('quit.html', firstName = user_data['first_name'], lastName = user_data['last_name'], email= user_data['email'], 
                           creatorFirst = creatorFirst, creatorLast = creatorLast, creatorEmail = creatorEmail)

def handle_message(message):
    if message == 1:
        return 'Yes, the college has a football team.'
    elif message == 2:
        return 'Yes, the college offers a Computer Science Major.'
    elif message == 3:
        return 'The in-state tuition for the college is $12000.'
    elif message == 4:
        return 'Yes, the college provides on-campus housing.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
