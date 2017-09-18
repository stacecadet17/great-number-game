from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "fantasia"

@app.route('/')
def index():
    session['correct'] = random.randrange(0, 101) #sets the correct randomized number
    session['message'] = "" #sets the variable for the message that will display depending on what happens
    print session['correct'] #just printing the random number to the console so that I know what it is
    return render_template('index.html')

@app.route('/lose')
def lose():
    return render_template('lose.html') #just setting up this page so we know where to go when we lose

@app.route('/win')
def win():
    return render_template('win.html') #just setting up this page so we know where to go when we win

@app.route('/result', methods=['POST'])
def result():
    session['guess'] = int(request.form['guess']) #getting the request that was submitted by the user
    if session['guess'] == session['correct']: #if the guess matches the correct number, then you win!
        session['message'] = "CORRECT, you win!"
        return redirect('/win') # have to redirect the the win page so we can be invited to play again
    else:
        if session['guess'] > session['correct']: # guess is higher than the randomized number
            session['message'] = "Too high"
            session['guess'] = request.form['guess'] #getting whatever number was submitted as a guess
            return redirect ('/lose') # have to redirect to the lose page so the message can display and we can be given another chance
        else:
            session['guess'] = request.form['guess']
            session['message'] = "Too low"
            return redirect ('/lose')

app.run(debug = True)
