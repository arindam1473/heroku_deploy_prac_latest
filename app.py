from flask import Flask, render_template, request,jsonify,redirect,url_for
import pymongo
import ssl
from deregister import cnvrt_blueprint
from db_connect import *
from register_user import register_user_blueprint
from login_user import *

app = Flask(__name__)
app.register_blueprint(cnvrt_blueprint)
app.register_blueprint(db_connect_blueprint)
app.register_blueprint(register_user_blueprint)
app.register_blueprint(login_user_blueprint)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')

'''
Requirments :
Changes V 1.0: This method will take values from index page cal calculate based on operation 
Changes V 1.1: We are keeping this below code as stand by for later use
Author : Arindam
'''
@app.route('/math', methods=['POST'])
def math_operations():
    result = ''
    operation = request.form['operation']
    try:
        num1 = int(request.form['num1'])
        if operation=='square':
            r = num1**2
            result = 'Square of '+str(num1)+' is : ' + str(r)
        if operation=='cube':
            r = num1**3
            result = 'Cube of '+str(num1)+' is : ' + str(r)
        if operation=='factorial':
            tmp = int(1)
            for i in list(range(num1, 1, -1)):
                tmp = tmp * i
            result = 'Factorial of '+str(num1)+' is : ' + str(tmp)
        if operation=='evod':
            if num1%2==0:
                r = 'Even'
            else:
                r = 'Odd'
            result = 'Your Entered Number '+str(num1)+' is : ' + r

    except Exception as e:
        print('In Except')
        return render_template('index.html')

    return render_template('results.html',result=result)






if __name__ == '__main__':
    app.run()