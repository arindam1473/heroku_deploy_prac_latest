from flask import Blueprint
import pymongo


db_connect_blueprint = Blueprint('mongo_db_connect_blueprint', __name__)


def connect_database():
    client = pymongo.MongoClient(
        "mongodb://raj:raj@cluster0-shard-00-00.txvde.mongodb.net:27017,cluster0-shard-00-01.txvde.mongodb.net:27017,cluster0-shard-00-02.txvde.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-13xnq3-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.test
    print('DB 1')
    db_lp = client['heroku_deploy_project']
    collection = db_lp['login_details']
    print('DB Connect')

    return collection  #Trying to return the connection