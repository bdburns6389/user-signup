from flask import Flask, request, redirect, render_template
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True

user_error = ""
pass_error = ""
match_error = ""
email_error = ""

@app.route("/input", methods=['POST'])
def welcome():
    username= request.form['username']
    password= request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    #if any are wrong, template will pass all of them
    if len(username) < 3 or len(username) > 20:
        user_error = "That's not a valid username."

    if len(password) < 3 or len(password) > 20:
        pass_error = "That's not a valid password."
    
    if password != verify_password:
        match_error = "Passwords don't match."
    
    if len(email) > 1:
        #works, but only called if everything else is valid.
        if "." not in email or "@" not in email or len(email) < 8 or len(email) > 28:
            email_error = "That's not a valid email."
    
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')
    
    


app.run()

