from flask import Flask,session,jsonify,render_template


app = Flask("ITsafe API Server", static_url_path='')
app.secret_key = "ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/get_number', methods=["GET"])
def get_number():

    if session.get("visit"):
        session["visit"] += 1
    else:
        session["visit"] =1

    return jsonify({"visit": session["visit"]})


debug = True
if __name__ == "__main__": 
   app.run(host='0.0.0.0', port=1337, debug=debug)
