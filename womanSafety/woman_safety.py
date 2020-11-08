from flask import Flask, request,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('Index.html')

@app.route('/drive')
def drive():
    return render_template('female_drivers.html')
@app.route('/ngo')
def ngo():
    return render_template('ngo.html')
@app.route('/selfdefence')
def defence():
    return render_template('SelfDefence.html')
@app.route('/legal')
def legal():
    return render_template('LegalAdvice.html')

if __name__ == '__main__':
    app.run()
