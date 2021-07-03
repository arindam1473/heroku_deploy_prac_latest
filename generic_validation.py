



def validate_username_passeord_from_db(username,password,collection,check_for):
    print('Checking : ' + str(username))
    print('Checking : ' + str(password))
    print('Checking : ' + str(collection))
    if check_for == 'fromregister':
        try:
            print('At least in try')
            for srch_usr in collection.find({'username': username}):
                if type(srch_usr) == dict:
                    print('usr found')
                    return str('flag1')  # Returning flag1 as username found in DB
        except Exception as e:
            print(e)
            print('Shit Happended')
        return str('flag0')
    elif check_for == 'fromlogin':
        for usr in collection.find({'username': username, 'password': password}):
            if type(usr) == dict:
                print('Checking usr.pass find in db')
                for key, val in usr.items():
                    if key == 'username':
                        result = 'Hello ' + str(val) + ' Nice to see you here again !!'
                        print(result)
                        return result
        else:
            return str('flag_login_error')

    elif check_for == 'fromderegister':
        for usr in collection.find({'username': username, 'password': password}):
            if type(usr) == dict:
                print('Checking usr.pass find in db')
                for key, val in usr.items():
                    if key == 'username':
                        query_to_delete_userdetails = {'username': username, 'password': password}
                        collection.delete_one(query_to_delete_userdetails)
                        result = 'Hello ' + str(val) + ' Good Bye !! Would like to see you again'
                        print(result)
                        return result
        else:
            return str('flag_login_error')

    else:
        return str('Generic Issue Occoured')
            #return render_template('errors.html', result='Your user not found')
