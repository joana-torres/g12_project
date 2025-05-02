from flask import Flask, render_template, request, session
from classes.user import User

prev_option = ""

def apps_user():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = User.current()
            User.remove(obj.id)
            if not User.previous():
                User.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(User.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["email"] + ';' + request.form["signup_date"]
            obj = User.from_string(strobj)
            User.insert(obj.id)
            User.last()
        elif prev_option == 'edit' and option == 'save':
            obj = User.current()
            obj.name = request.form["name"]
            obj.dob = request.form["email"]
            obj.salary = request.form["signup_date"]
            User.update(obj.id)
        elif option == "first":
            User.first()
        elif option == "previous":
            User.previous()
        elif option == "next":
            User.nextrec()
        elif option == "last":
            User.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = User.current()
        if option == 'insert' or len(User.lst) == 0:
            id = 0
            id = User.get_id(id)
            name = email = signup_date = ""
        else:
            id = obj.id
            name = obj.name
            email = obj.email
            signup_date = obj.signup_date
        return render_template("user.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,email=email,signup_date=signup_date, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

