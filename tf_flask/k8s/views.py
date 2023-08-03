from wsgi import app
from flask import render_template

# The .route() function in flask is a decorator that tells the application what function to run when visiting certain URLs.
# This defines that when someone visits <URL>/ the hello_world application should run
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/navbar.html')
def navbar():
    return render_template('navbar.html')

@app.route('/templates/header.html')
def header():
    return render_template('header.html')