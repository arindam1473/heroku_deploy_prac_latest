from flask import request,render_template,Flask,Blueprint
from db_connect import connect_database
from generic_validation import validate_username_passeord_from_db

cnvrt_blueprint = Blueprint('cnvrt_blueprint_name', __name__)

@cnvrt_blueprint.route('/deregister' ,methods=['POST'])
def deregister_user():
    dereg_usrname= request.form['dereg_usrname']
    dereg_usrpaswrd = request.form['dereg_usrpaswrd']
    if not dereg_usrname or not dereg_usrpaswrd:
        return render_template('errors.html', result='Blank User/Password Not Allowed')
    print(str(dereg_usrname))
    collection = connect_database()
    result = validate_username_passeord_from_db(dereg_usrname,dereg_usrpaswrd,collection,'fromderegister')
    if result != 'flag_login_error':
        return render_template('errors.html',result=result)
    else:
        return render_template('errors.html',result='Your Username/Password Not Found')

    #CRUD operation in Python,
    #Crete using pymongo