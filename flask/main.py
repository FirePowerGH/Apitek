from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form["username"]
    password = request.form["password"]

    if username.lower() == "bibliotekar":
        if password == "bok":
            return redirect(url_for("biblio"))
        else:
            return "wrong password"
    else:
        return redirect(url_for("utlan"))

@app.route("/kontrollpanel")
def biblio():
    return render_template("biblio.html")

@app.route("/utlan")
def utlan():
    return render_template("utlan.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")