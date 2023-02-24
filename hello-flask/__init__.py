from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import session
from flask import render_template

from markupsafe import escape


app = Flask(__name__)

# TEMPORARY
# Set the secret key to some random bytes. Keep this really secret!
# TO DO: How to automatically generate this?
#   or is there a safer and secure way of generating the session key?
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    # check if session variable exist and not empty
    if 'username' in session:
        # display index page
        return render_template('index.html', username=session['username'])

    # redirect to login page
    return redirect(url_for('login'))

# source: https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
@app.route('/login', methods=['GET', 'POST'])
def login():
    # this will contain the error message
    error = None

    # if the request method is POST,
    if request.method == 'POST':
        # let's perform a very very very basic user authentication
        # this is done by checking the for fields (username and password) 
        # against a hard coded user name and password
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # set the error if the credential is invalid
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = 'Admin'
            return redirect(url_for('index'))
        
    return render_template('login_form.html', error=error)

# logout
# clear username
@app.route('/logout')
def logout():
    # let's empty the session
    session.pop('username', None)
    # then route back to index page
    # which will be routed to log in
    return redirect(url_for('index'))

# Page Not Found Error Handler
@app.errorhandler(404)
def page_not_found(error):
    # display this template if page is not found
    return render_template('page_not_found.html'), 404