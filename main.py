from flask import Flask, request, redirect, render_template
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True

user_error = "That's not a valid username."
pass_error = "That's not a valid password."
match_error = "Passwords don't match."
email_error = "That's not a valid email."

@app.route("/input", methods=['POST'])
def welcome():
    username= request.form['username']
    password= request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    if len(username)< 1:
        return render_template('index.html', user_error=user_error)

    elif len(password) < 1:
        return render_template('index.html', pass_error=pass_error)
    
    elif password != verify_password:
        return render_template('index.html', verify_error=match_error)
    
    else:
        return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')
    
    


app.run()

"""If both fields are correct, works correctly.  if """