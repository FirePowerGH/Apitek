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

@app.route("/utlan", methods=["GET", "POST"])
def utlan():
    if request.method == "GET":
        return render_template("utlan.html", )

@app.route("/kontrollpanel", methods=["GET", "POST"])
def biblio():
    tabell = int(request.args.get('tabell', 1))
    if request.method == "GET":
        return render_template("biblio.html", tabell=tabell)

    if tabell == 1:
        return redirect(url_for("biblio", tabell=2))
    else:
        return redirect(url_for("biblio", tabell=1))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")