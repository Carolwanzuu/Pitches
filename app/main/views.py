from flask import render_template
from app import app

@main.route('/')
def index():
    '''
    viewing root page function
    '''
    return render_template('index.html')
    