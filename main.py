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
    #if any are wrong, template will pass all of them
    if len(username) < 3 or len(username) > 20:
        return render_template('index.html', user_error=user_error, username=username)

    if len(password) < 3 or len(password) > 20:
        return render_template('index.html', pass_error=pass_error, username=username)
    
    if password != verify_password:
        return render_template('index.html', verify_error=match_error)
    
    if len(email) > 1:
        #works, but only called if everything else is valid.
        if "." not in email or "@" not in email or len(email) < 8 or len(email) > 28:
            return render_template('index.html', email_error=email_error)
    
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')
    
    


app.run()

#Make sure to put username=username/email=email in rendertemplate of all
#elif's so that it is kept as data in the fields.  Passwords go away is fine.