'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask

application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])

def index():
    return "Hello, world!"

if __name__ == '__main__':
    app = application.run(host='0.0.0.0', port=8000)
