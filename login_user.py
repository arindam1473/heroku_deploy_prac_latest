from flask import Blueprint,render_template,request
from db_connect import connect_database
from generic_validation import validate_username_passeord_from_db

login_user_blueprint = Blueprint('login_user_blueprint_functions_handler', __name__)


@login_user_blueprint.route('/login', methods=['POST'])
def login_handler():
    print('Trying to fetch user')
    username = request.form['lgn_username']
    password = request.form['lgn_password']
    if not username or not password:
        return render_template('errors.html', result='Blank User/Password Not Allowed')
    collection = connect_database()
    result = validate_username_passeord_from_db(username, password, collection,'fromlogin')
    if result == 'flag_login_error':
        return render_template('errors.html', result='Username/Password Not matched')
    else:
        return render_template('welcome.html', result=result)

'''
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
    return str('flag_login_error')
'''
