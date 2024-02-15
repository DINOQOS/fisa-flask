## forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField # ****, 정규식 검증
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask import g
class QuestionForm(FlaskForm):
	                # 화면에서 출력할 해당 필드의 라벨, 필수 항목 체크 여부
    # <label for='subject'> 제목 </label>
    # <input type=text name='subject' required> 
    subject = StringField('제목', validators=[DataRequired()])

    # <label for='content'> 내용 </label>
    # <input typt=text-area name='content' required> 

    content = TextAreaField('내용', validators=[DataRequired()])
    
    #user_id = StringField('아이디', default=g.user.username)

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    # <label for='subject'> 비밀번호 확인 </label>
    # <input type=text name='subject' required> 
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=5, max=8)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):   
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=5, max=8, message="ID는 5글자 이상 8글자 미만이어야 합니다")])
    password = PasswordField('비밀번호', validators=[DataRequired()])
   