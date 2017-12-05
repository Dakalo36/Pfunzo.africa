from app import app
from flask import Flask, request, render_template, redirect, url_for
from .forms import SignupForm, LoginForm
from .models import db, User
from flask_login import LoginManager, login_user, login_required, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(firstname):
    return User.query.filter_by(firstname = firstname).first()


@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/protected')
@login_required
def protected():
    return "protected area"

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(firstname=form.Firstname.data).first():
                return "User address already exists"
            else:
                newuser = User(firstname=form.Firstname.data, lastname=form.Lastname.data,
                                age=form.Age.data, grade=form.Grade.data,
                                school=form.School.data, password=form.Password.data)
                db.session.add(newuser)
                db.session.commit()
                login_user(newuser)
                return "User created!!!"        
        else:
            return "Form didn't validate"

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user=User.query.filter_by(irstname=form.Firstname.data).first()
            if user:
                if user.password == form.Password.data:
                    login_user(user)
                    return "User logged in"                
                else:
                    return "Wrong password"            
            else:
                return "user doesn't exist"        
        else:
            return "form not validated"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"
   
def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

init_db()