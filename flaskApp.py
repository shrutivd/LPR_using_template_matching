from flask import Flask, render_template, request
import newDriver as nd

app = Flask(__name__)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    return render_template('frontend/register.html')

@app.route('/registered', methods = ['POST', 'GET'])
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

@app.route('/extract', methods = ['POST', 'GET'])
def extract():
    return render_template('frontend/extract.html')

@app.route('/extracted', methods = ['POST', 'GET'])
def extracted():
    return render_template('frontend/extracted.html')

@app.route('/')
def home():
    return render_template('frontend/home.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)