# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

import sqlite3 as sql
app = Flask(__name__)

user_email = "unknown"
user_pass = "secret"
loggedUser = False

suppliers = [{"name":"Tay loy","urlCall":"/supplier?name=tayloy"},{"name":"Crisol","urlCall":"/supplier?name=crisol"},{"name":"El Saber","urlCall":"/supplier?name=elSaber"}]

@app.route('/')
def home():
	loggedUser = False
	return render_template('index.html',Suppliers=suppliers)

@app.route('/supplier',methods=['GET'])
def supplier():
	supplier_name = request.args.get('name')
	supplier_imgPath = '/static/Images/noSupplier.png'
	supplier_products = [{"name":"nothing","urlCall":"noProduct.png"}]
	print supplier_name
	
	if supplier_name is 'tayloy':
		print "ARRIVED HERE"
		supplier_name = 'Tay Loy'
		supplier_imgPath = '/static/Images/t5.png'
		supplier_products = [{"name":"Archivador","urlCall":"/static/Images/27.jpg"},{"name":"Crayones","urlCall":"/static/Images/28.jpg"},{"name":"Papel a4","urlCall":"/static/Images/30.jpg"},{"name":"Laptop","urlCall":"/static/Images/25.jpg"}]
	if loggedUser:
		return render_template('supplierLogged.html', Email = user_email, Supplier_name = supplier_name, Supplier_imgPath = supplier_imgPath, Products = supplier_products, Suppliers = suppliers)
	
	return render_template('supplier.html', Supplier_name = supplier_name, Supplier_imgPath = supplier_imgPath, Products = supplier_products, Suppliers = suppliers)

@app.route('/about')
def about():
	if loggedUser:
		return render_template("aboutLogged.html", Email=user_email, Password = user_pass, Suppliers = suppliers)
	else:
		return render_template('about.html', Suppliers = suppliers)

@app.route('/logUser', methods=['POST','GET'])
def logUser():
	global user_email,user_pass,loggedUser
	if request.method == 'POST':
		try:
			email = request.form['Email']
			password = request.form['Password']
			user_email = email
			user_pass = password
			loggedUser = True
			# connect to database
			msg = "Record successfully added"
		except:
			msg = "error in insert operation"
			uid = '-1'
		finally:
			#con.close()
			return render_template("user.html", Email=email, Password = password, Suppliers = suppliers)

@app.route('/user')
def user():
	return render_template("user.html", Email=user_email, Password = user_pass, Suppliers = suppliers)

@app.route('/registerUser', methods=['POST','GET'])
def registerUser():
	global user_email,user_pass,loggedUser
	if request.method == 'POST':
		try:
			name = request.form['Name']
			email = request.form['Email']
			password = request.form['Password']
			rpassword = request.form['rPassword']
			user_email = email
			user_pass = password
			loggedUser = True
			# connect to database
			msg = "Record successfully added"
		except:
			msg = "error in insert operation"
			uid = '-1'
		finally:
			#con.close()
			return render_template("user.html", Email=user_email, Password = user_pass, Suppliers = suppliers)

@app.route('/icons')
def icons():
    return render_template('icons.html')

@app.route('/codes')
def codes():
    return render_template('codes.html')

@app.route('/mail')
def mail():
	if loggedUser:
		return render_template('mailLogged.html', Email =user_email, Password = user_pass, Suppliers = suppliers)	
	return render_template('mail.html', Suppliers = suppliers)

@app.route('/schools')
def schools():
	if loggedUser:
		return render_template('schoolsLogged.html', Email =user_email, Password = user_pass, Suppliers = suppliers)	
	return render_template('schools.html', Suppliers = suppliers)

@app.route('/schoolLists',methods=['GET'])
def schoolLists():
	school_name = request.args.get('name')
	supplier_imgPath = '/static/Images/noSupplier.png'
	supplier_products = [{"name":"nothing","urlCall":"noProduct.png"}]
	
	if loggedUser:
		return render_template('schoolListsLogged.html', Email = user_email, School_name = school_name, Suppliers = suppliers)
	return render_template('schoolLists.html', School_name = school_name, Suppliers = suppliers)


@app.route('/kindergarden')
def kindergarden():
	if loggedUser:
		return render_template('kindergardenLogged.html', Email =user_email, Password = user_pass, Suppliers = suppliers)	
	return render_template('kindergarden.html', Suppliers = suppliers)

@app.route('/kinderLists',methods=['GET'])
def kinderLists():
	kinder_name = request.args.get('name')
	supplier_imgPath = '/static/Images/noSupplier.png'
	supplier_products = [{"name":"nothing","urlCall":"noProduct.png"}]
	
	if loggedUser:
		return render_template('kindergardenListsLogged.html', Email = user_email, Kinder_name = kinder_name, Suppliers = suppliers)
	return render_template('kindergardenLists.html', Kinder_name = kinder_name, Suppliers = suppliers)

@app.route('/others')
def others():
	if loggedUser:
		return render_template('othersLogged.html', Email =user_email, Password = user_pass, Suppliers = suppliers)	
	return render_template('others.html', Suppliers = suppliers)

@app.route('/orderLists',methods=['GET'])
def orderLists():
	school_name = request.args.get('name')
	supplier_imgPath = '/static/Images/noSupplier.png'
	supplier_products = [{"name":"nothing","urlCall":"noProduct.png"}]
	
	if loggedUser:
		return render_template('orderListsLogged.html', Email = user_email, School_name = school_name, Suppliers = suppliers)
	return render_template('orderLists.html', School_name = school_name, Suppliers = suppliers)

if __name__ == '__main__':
    app.run(debug = True)
