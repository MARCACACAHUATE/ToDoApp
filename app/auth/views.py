#BluePrint
from . import auth
#Forms
from app.forms import LoginForm
#Templates
from flask import render_template


@auth.route('/login', methods = ['POST','GET'])
def login():
    context = {
        "login_form": LoginForm()
    }

    return render_template('login.html', **context)