from flask import Flask

'''
app is that we have import the instance or create the instance of the flask app,
which will be your WSGI (Web Server Gateway Application) application
'''
### WSGI application
app = Flask(__name__)

@app.route('/')

def welcome():
    return 'Welcome to our page'

if __name__=='__main__':
    app.run()