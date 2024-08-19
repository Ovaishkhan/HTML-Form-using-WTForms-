from flask import Flask, flash, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap, Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('assword', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('LogIn')


app = Flask(__name__)
app.secret_key = "any-secret-key-you want to create"
"""secret key is required for using csrfq3w"""
bootstrap = Bootstrap5(app) #initialise bootstrap-flask


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        print(login_form.password.data)
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else: return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
