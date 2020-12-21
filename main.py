from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
import playsound

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
       user = request.form["nm"]
       session["user"] = user
       flash("You have been logged in")
       return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("email has been submitted")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1',port='3000')