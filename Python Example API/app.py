from flask import Flask, jsonify, request
#import urllib3
import json
import datetime
from waitress import serve
from impactmodel import impact
import codecs
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

USER_DATA = {
"admin": "stella123456"
}

@auth.verify_password
def verify(username, password):
	if not (username and password):
		return False
	return USER_DATA.get(username) == password

@app.route('/ImpactModel',methods =['GET','POST'])
@auth.login_required
def impactmodelfunction():
    input_json = request.get_json(force=True)
    ip = request.remote_addr
    ts = datetime.datetime.now()
    csvfile = codecs.open("F:\\Flask Stack\\ImpactModel\\Logs\\Interaction_logs.txt",'a','utf-8')
    csvfile.write(str(ip) + ',' + str(ts) + "\n")
    csvfile.close()

    try:
    	test = impact(input_json)
    except Exception as e:
	csvfile = codecs.open("F:\\Flask Stack\\ImpactModel\\Logs\\Error_log.txt",'a','utf-8')
	csvfile.write(str(e) + '\n')
        csvfile.close()

    return jsonify(test)

if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=5025)

#@app.route('/')
#def index():
    #return("HELLO TEST")
