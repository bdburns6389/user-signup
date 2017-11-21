from flask import Flask, request, redirect, render_template
import cgi
import re



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/input", methods=['POST'])
def welcome():
    username= request.form['username']
    password= request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    pattern = r"[A-z0-9]+@[A-z0-9]+\.[A-z0-9.]+"
    
    if len(username)< 1:
        error = "Please enter valid username"
        return render_template('index.html', error=error)

    elif len(password) < 1:
        pass_error= "Too Short of a Password"
        return render_template('index.html', pass_error=pass_error)
    
    elif password != verify_password:
        verify_error= "Passwords don't match!"
        return render_template('index.html', verify_error=verify_error)
    
    elif not re.match(pattern, email):
        email_error = "Invalid email"
        return render_template('index.html', email_error=email_error)

    else:
        return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')
    
    


app.run()

"""If both fields are correct, works correctly.  if """