from flask import Blueprint,render_template,request
from db_connect import connect_database
from generic_validation import validate_username_passeord_from_db

register_user_blueprint = Blueprint('register_user_blueprint_name', __name__)


@register_user_blueprint.route('/register',methods=['POST'])
def register_handler():
    register = str(request.form['register'])
    username = str(request.form['reg_usrname'])
    password = str(request.form['reg_password'])
    print('got usr pass')
    if not username or not password:
        return render_template('errors.html', result='Blank User/Password Not Allowed')
    else:
        allowedornot = True
    print('Continue as BAU Code as : ' + str(allowedornot))
    try:
        print('Trying to register')
        collection = connect_database()
        print("Somethig issue ?")
        get_flag = validate_username_passeord_from_db(username, password, collection,'fromregister')

        print(get_flag)
        if get_flag == 'flag1':
            return render_template('errors.html', result='You are already registered, Please Login')
        elif get_flag == 'flag0':
            insert_new_user(username, password, collection)
            return render_template('welcome.html', result='Welcome ' + str(username) + ' Hope you are fine')
        elif get_flag == 'flag_error':
            return render_template('errors.html', result=str('You are not allowed,Please Sign-up/Register properly'))
        print('Con DB')
    except Exception as e:
        result = 'Register is not Successful..'
        return render_template('errors.html', result=result)

def insert_new_user(username,password,collection):
    print('in except')
    ins_record = {
        'username': username,
        'password': password
    }

    collection.insert_one(ins_record)
    print('in reg usr last')
    return str('flag0')
'''
def register_user(username,password,collection):
    print('Registering'+ str(username))
    print('Registering' + str(password))
    print('Registering' + str(collection))
    try:
        print('At least in try')
        for srch_usr in collection.find({'username':username}):
            if type(srch_usr)==dict:
                print('usr found')
                return str('flag1') #Returning flag1 as username found in DB
    except Exception as e:
        print(e)
        print('Shit Happended')

    return str('flag0')
'''