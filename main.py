from flask import Flask,jsonify,abort,render_template
from flask_restful import Resource,Api,request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)
api=Api(app)
tasks=[]
auth = HTTPBasicAuth()
users = {
    "harsha": generate_password_hash("yamaha")
}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    else:
        return "<h4>Incorrect username or password</h4>"
@app.route('/')
@auth.login_required
def index():
    return render_template("index.html")
@app.route("/put/<string:name>",methods=["POST","GET"])
def post(name):
    temp={"data":name}
    tasks.append(temp)
    return {"note":"added"}
@app.route("/post/<string:name>",methods=["GET"])
def get(name):
    if request.method=="GET":
        for x in tasks:
            if x["data"]==name:
                return x
            else:
                return ({"data":"none"})

@app.route("/rest/<string:name>",methods=["GET","POST"])
def delete(name):
    for ind,x in enumerate(tasks):
        if x["data"] == name:
            tasks.pop(ind)
            return ({"NOTE":"deleted"})
@app.route("/draw/<string:name>/<string:surname>",methods=["GET","POST","PUT"])
def update(name,surname):
    for ind,x in enumerate(tasks):
        if x["data"] == name:
            x["data"]=surname
            return tasks
if (__name__)=="__main__":
    app.run(debug=True)