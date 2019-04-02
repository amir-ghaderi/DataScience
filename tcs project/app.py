from flask import Flask, render_template, jsonify, request
from waitress import serve

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


#Get Data
@app.route('/randomforestmodel', methods=["GET","POST"])
def modeldata():
    print('hello')
    input_json = request.get_json(force=True)

    businesscomplexity = input_json['businesscomplexity']
    businesscriticality = input_json['businesscriticality']
    technologicalcomplexity = input_json['technologicalcomplexity']
    incidents = input_json['incidents']
    releases = input_json['releases']
    interfaces = input_json['interfaces']

    print(businesscomplexity)

    print(businesscriticality)
    print(technologicalcomplexity)
    print(incidents)
    print(releases)
    print(interfaces)


    return jsonify( {"date" : "closse" , "close" : "closaae"  }) 
    

if __name__ == "__main__":
    app.run(debug=True)
    serve(app, host='0.0.0.0')






















