from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')

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