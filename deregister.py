from flask import request,render_template,Flask,Blueprint


cnvrt_blueprint = Blueprint('cnvrt_blueprint_name', __name__)

@cnvrt_blueprint.route('/deregister' ,methods=['POST'])
def deregister_user():
    dereg_usrname= request.form['dereg_usrname']
    print(str(dereg_usrname))
    return render_template('errors.html',result='Error')

    #CRUD operation in Python,
    #Crete using pymongo