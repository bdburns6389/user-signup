from flask import Flask, request, redirect, render_template
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/input", methods=['POST'])
def welcome():
    username= request.form['username']
    password= request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    user_error = ""
    pass_error = ""
    match_error = ""
    email_error = ""
    
    if len(username) < 3 or len(username) > 20:
        user_error = "That's not a valid username."

    if len(password) < 3 or len(password) > 20:
        pass_error = "That's not a valid password."
    
    if password != verify_password:
        match_error = "Passwords don't match."
    
    if len(email) > 1:
        if "." not in email or "@" not in email or len(email) < 8 or len(email) > 28:
            email_error = "That's not a valid email."
    
    if user_error = "" and pass_error = "" and match_error = "" and email_error = "":
        return render_template('welcome.html', username=username)
    else: 
        return render_template('index.html', username=username, email=email, user_error=user_error, pass_error=pass_error, match_error=match_error, email_error=email_error)

@app.route("/")
def index():
    return render_template('index.html')
    
    


app.run()

