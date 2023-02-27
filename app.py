from flask import Flask, render_template, request
from os import environ

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
    
    return render_template('login.html')

def main():
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()