# AS simeple as possbile flask google oAuth 2.0
from flask import Flask, redirect, url_for, session
import os
from datetime import timedelta
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory


# App config
app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")


@app.route('/googleSigninData',methods=['GET','POST'])
def googleSigninData():
	authProvider=request.form['authProvider']
	googleTockenId=request.form['googleTockenId']
	Firstname=request.form['Firstname']
	Lastname=request.form['Lastname']
	email=request.form['email']

	print(authProvider)
	print(googleTockenId)
	print(Firstname)
	print(Lastname)
	print(email)
	send_data = {'success': True,'googleTockenId':googleTockenId,'Firstname':Firstname,'Lastname':Lastname,'email':email}
	return make_response(jsonify(send_data), 200)



@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)
