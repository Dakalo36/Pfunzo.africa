from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired

class SignupForm(Form):
    Firstname = StringField('First Name',
                    validators=[DataRequired()])
    Lastname = StringField('Last Name',
                    validators=[DataRequired()])
    Age = StringField('Age',
                    validators=[DataRequired()])
    Grade = StringField('Grade',
                    validators=[DataRequired()])
    School = StringField('School',
                    validators=[DataRequired()]) 
    Password = PasswordField(
                'password', 
                validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(Form):
    Username = StringField('UserName',
                    validators=[DataRequired()])
    Password = PasswordField('Password',
                    validators=[DataRequired()])
    submit = SubmitField("Sign In")
    
