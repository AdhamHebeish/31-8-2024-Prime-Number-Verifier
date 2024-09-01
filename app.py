from flask import Flask, render_template, request
import os

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify',methods=['POST'])
def verify():
    result = ""
    num = request.form['number']
    posnum = num.replace("-","")
    if posnum.isnumeric() == False:
        result = "You have entered a non-number or a decimal."
    else:
        num = int(num)
        if num <= 0:
            result = "Please enter a positive integer."
        elif num < 3:
            numstr = str(num)
            result = numstr + " is a prime number."
        else:
            for x in range(2, num):
                divx = num % x
                if divx == 0:
                    numstr = str(num)
                    result = numstr + " is not a prime number and is composite."
                    break
                else:
                    numstr = str(num)
                    result = numstr + " is a prime number."
    return render_template("index.html", result = result)

if __name__ == '__main__':
    app.run()
