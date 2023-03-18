from flask import Flask, render_template, request
import newDriver as nd
import app

flaskApp = Flask(__name__)

@flaskApp.route('/register', methods = ['POST', 'GET'])
def register():
    return render_template('frontend/register.html')

@flaskApp.route('/registered', methods = ['POST', 'GET'])
def registered():
    if request.method == "POST":
       fname = request.form.get("firstName")
       lname = request.form.get("lastName")
       state = request.form.get("state")
       lp = request.form.get("licensePlate")
       email = request.form.get("email")
       number = request.form.get("phone")
       bday = request.form.get("birthday")

       nd.registerNewDriver(state, lp, fname, lname, email, number, bday)
       
    return render_template('frontend/registered.html')

@flaskApp.route('/extract', methods = ['POST', 'GET'])
def extract():
    return render_template('frontend/extract.html')

@flaskApp.route('/extracted', methods = ['POST', 'GET'])
def extracted():
    if request.method == "POST":
        file = request.form.get("file")
        fast = request.form.get("fast")
        info_li = app.mainFrontend('static/images/' + file, fast)
        # name, state, symbols, email, phone, bday
        if len(info_li) > 2:
            return render_template('frontend/extracted.html', name=info_li[0], bday=info_li[5], state=info_li[1], symbols=info_li[2], email=info_li[3], phone=info_li[4], file=file)
        else:
            return render_template('frontend/almostextracted.html', state=info_li[0], symbols=info_li[1], file=file)

@flaskApp.route('/')
def home():
    return render_template('frontend/home.html')

if __name__ == "__main__":
    flaskApp.run(host='127.0.0.1', port=5002)