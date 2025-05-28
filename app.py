from flask import Flask, render_template, request, session
from classes.user import User
from datafile import filename
from classes.post import Post
from classes.topic import Topic
from classes.user_post import User_Post
from classes.userlogin import Userlogin
from subs.apps_user import apps_user
from subs.apps_gform import apps_gform
from subs.apps_subform import apps_subform
from subs.apps_plotly import apps_plotly
from subs.apps_userlogin import apps_userlogin
#from subs_userFoto import userfsub
import os


app = Flask(__name__)

User.read(filename + 'socialmedia.db')
Topic.read(filename + 'socialmedia.db')
Post.read(filename + 'socialmedia.db')
User_Post.read(filename + 'socialmedia.db')
Userlogin.read(filename + 'socialmedia.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'


upload_folder = os.path.join('static', 'fotos')

app.config['UPLOAD'] = upload_folder


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)
@app.route("/User", methods=["post","get"])
def user():
    return apps_user()
@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)

@app.route("/plotly", methods=["post","get"])
def plotly():
    return apps_plotly()
@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()

# @app.route("/user_foto", methods=["post","get"])
# def gformFoto():
#     cname = "User"
#     return userfsub.userFotoform(app,cname)

if __name__ == '__main__':
    app.run()
    
