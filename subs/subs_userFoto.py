# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gform.py

"""""
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import os

from classes.user import User

prev_option = ""
img = ""



def userFotoform(app,cname=''):
    global img
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            
            file = request.files['img']
            filename = secure_filename(file.filename)
            foto = filename
            if foto != "" :
                
                file.save(os.path.join(app.config['UPLOAD'], filename))

                
            for i in range(1,len(cl.att)):
                att = cl.att[i]
                if att != '_foto':
                    strobj += ";" + request.form[cl.att[i]]
                else:
                    strobj += ";" + foto
                    
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            
            file = request.files['img']
            filename = secure_filename(file.filename)
            foto = filename
            if foto != "" and foto != obj._foto:
                
                file.save(os.path.join(app.config['UPLOAD'], filename))

            else:
                foto = obj._foto
            
            for i in range(cl.auto_number,len(cl.att)):
                att = cl.att[i]
                if att != '_foto':
                    setattr(obj, att, request.form[att])
                else:
                    setattr(obj, att, foto)
                    
                
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
            img = os.path.join(app.config['UPLOAD'], "None.png")    
        else:
            
            if obj._foto == "" or obj._foto == "None":
                img = os.path.join(app.config['UPLOAD'], "None.png") 
            else:
                img = os.path.join(app.config['UPLOAD'], obj._foto)
                
                
            print("obj._foto>>>>>>",obj._foto)
        return render_template("user_foto.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        img=img)
    else:
        return render_template("index.html", ulogin=ulogin)
