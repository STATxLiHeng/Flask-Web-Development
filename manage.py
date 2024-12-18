from flask import Flask, url_for, render_template,request
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
    # Migrate_Command
from flask_script import Manager,Command

app = Flask(__name__)
app.config['SECRET_KEY'] = 'daxiong'
# 調適模式 (開發一定要開)
# app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:ki2357968@localhost/flask_demo')
app.config['SOLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
#繼承commond
class Hello(Command):
    def run(self):
        print('hello world')

manager.add_command('hello',Hello())
# manager.add_command('db',Migrate_Command)
# @manager.command
# def hi():
#     print('andy')

# class User():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         return f'<h3>我的名字是{self.name}, 年齡是{self.age}</h3>'
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    gender = db.Column(db.Boolean,default=True)
    hobby = db.Column(db.String(120))
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    articles = db.relationship('Article', backref='user')

    def __repr__(self):
        return f"<User> is {self.username}"

class Article(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(80),unique=True,nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #關聯

    def __repr__(self):
        return f"<Article> is {self.title}"

@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    # if request.method == 'POST' and  form.validate():
    if form.validate_on_submit():
        pass
    return render_template('login.html',form =form)

@app.route('/')
def index():
    dict_val = {'name':'andy','age':18}
    list_val = [i for i in range(10)]
    user = User('mai',18)
    return render_template('index.html',info = dict_val, number =list_val,user=user)

@app.route('/user/<username>')
def show_user_info(username):
    return render_template('user.html',name = username)

@app.route('/post/<int:post_id>')
def show_post_info(post_id):
    return f'post_id是{post_id}'

# @app.route('/login', methods=['GET','POST'])
# def login():
#     return f'get 請求'

# 找到url 生成連結
@app.route('/test')
def test():
    return url_for('show_user_info',username='mai')

if __name__ == "__main__":
    #調適模式
    # app.run(debug=True,
    # #         port = 8000)
    # app.app_context().push()
    # db.create_all()
    manager.run()