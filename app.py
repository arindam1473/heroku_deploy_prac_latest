from flask import Flask, render_template, request,jsonify
import pymongo
import ssl


app = Flask(__name__)

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

@app.route('/signinchooser', methods=['POST'])
def login_page():
    signinchoose = str(request.form['signinchoose'])
    username = str(request.form['username'])
    password = str(request.form['password'])
    print('got usr pass')
    usr_nm='kothay vai'
    if signinchoose == 'register':
        try:
            print('Trying to register')
            usr_nm = connect_database(username,password,signinchoose)
            print('Con DB')
        except Exception as e:
            result = 'Register is not Successful..'
            return render_template('errors.html',result=result)
    elif signinchoose== 'login':
        print('Trying to fetch user')
        result = connect_database(username, password,signinchoose)
        return render_template('welcome.html', result=result)

    return render_template('results.html', result=usr_nm)


def connect_database(username,password,signinchoose):
    client = pymongo.MongoClient(
        "mongodb://raj:raj@cluster0-shard-00-00.txvde.mongodb.net:27017,cluster0-shard-00-01.txvde.mongodb.net:27017,cluster0-shard-00-02.txvde.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-13xnq3-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.test
    print('DB 1')
    db_lp = client['heroku_deploy_project']
    collection = db_lp['login_details']
    print('DB Connect')
    if signinchoose=='register':
        ins_record={
            'username':username,
            'password':password
        }
        collection.insert_one(ins_record)
    elif signinchoose == 'login':
        print('In Login')
        res = verify_user_pass(username,password,collection)
        print(res)
        return res


    return str(username)

def verify_user_pass(username,password,collection):
    for usr in collection.find({'username': username, 'password': password}):
        if type(usr) == dict:
            print('Checking usr.pass find in db')
            for key, val in usr.items():
                if key == 'username':
                    result = 'Hello ' + str(val) + ' Nice to see you here again !!'
                    print(result)
                    return result
        else:
            return render_template('errors.html', result='Your user not found')





if __name__ == '__main__':
    app.run()