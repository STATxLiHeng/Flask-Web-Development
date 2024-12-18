from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField(label ='用戶名',validators = [
                DataRequired('請填寫用戶名'),
                Length(min=6, max=50, message='用戶名長度請大於6')])

    password = PasswordField(label = '密碼', validators = [
                DataRequired('請填寫密碼'),
                Length(min=6, max=50)])

    submit = SubmitField(label = '提交')