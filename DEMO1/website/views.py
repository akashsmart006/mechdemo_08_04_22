from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from sqlalchemy import asc, desc
views = Blueprint('views',__name__)

@views.route('/')
def base():
    return render_template("base.html")
@views.route('/home1',methods=['GET','POST'])
def home1():
    return render_template("home1.html")
@views.route('/home2',methods=['GET','POST'])
def home2():
    mname=""
    mnum=""
    if request.method=='POST':
        lat=request.form.get('lat')
        lon=request.form.get('lon')
        lat=float(lat)
        lon=float(lon)
        print(lat)
        print(lon)
        k=10000
        mechus=User.query.filter_by(usertype="mechanic").all()
        for i in mechus:
            ln=(i.lon)[0:5]
            lt=(i.lat)[0:5]
            if len(ln)>0:
                if(float(ln)-lon<k):
                    k=float(ln)-lon
                    mname="Nearby Mechanic Is Mr."+i.name
                    mnum="Mobile : "+i.mobile
    return render_template("home2.html",mname=mname,mnum=mnum)
@views.route('/home3')
def home3():
    return render_template("home3.html")
@views.route('/home4')
def home4():
    return render_template("home4.html")
@views.route('/home5')
def home5():
    return render_template("home5.html")