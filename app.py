from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

my_client = MongoClient("localhost", 27017)
my_db = my_client["college"]
students = my_db["students"]
callme = my_db["callme"]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/campus", methods=["GET"])
def campus():
    return render_template("campus.html")

@app.route("/admissions", methods=["GET"])
def admissions():
    return render_template("admissions.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        _id = int(request.form["id"])
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        percentage = request.form["percentage"]
        rank = int(request.form["rank"])
        course = request.form["course"]
        address = request.form["address"]

        students.insert_one({
            "id":_id, "name":name, "email":email, "phone":phone, "percentage":percentage, 
            "rank":rank, "course":course, "address":address
        })
        return redirect("/register")
    else:
        return render_template("register.html")

@app.route("/view", methods=["GET"])
def view():
    raw = list(students.find())
    return render_template("view.html", output=raw)

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        _id = int(request.form["id"])
        field = request.form["field"]
        new_data = request.form["new_data"]
        students.update_one(
            {"id":_id}, {"$set":{field:new_data}}
        )
        return redirect("/update")

    else:
        return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        _id = int(request.form["id"])
        students.delete_one({"id":_id})
        return redirect("/delete")
    else:
        return render_template("delete.html")

@app.route("/callme", methods=["POST"])
def callme_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["num"]
    course = request.form["course"]
    callme.insert_one({
        "name":name, "email":email, "phone":phone, "course": course
    })
    return redirect("/")

app.run(debug=True)
