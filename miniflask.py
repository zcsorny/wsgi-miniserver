''' Mini flask app that will be deployed on Nginx '''
import config   # importing in private env.vars 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'The app is working'

if __name__=='__main__':
    app.run(debug=True,host=config.HOST)
