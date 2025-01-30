from flask import Flask, render_template, request, redirect, url_for, jsonify
from api import Database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

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

@app.route("/register", methods=["GET", "POST"])
def register():
    names = Database.fetchNames()
    return render_template("register.html", names=names)

@app.route("/utlan", methods=["GET"])
def utlan():
    # if request.method == "GET":
    #     return render_template("utlan.html", )

    try:
        bokID = int(request.args.get('bokid', 1))
        tittel = Database.getBooksFromDb(bokID)[0][1]
        forf = Database.getBooksFromDb(bokID)[0][2]
    except Exception as e:
        return jsonify({"error": f"mysql error: {e}"})
    finally:
        if tittel != None or tittel != "" and forf != None or forf != "":
            return render_template("utlan.html", title=tittel, author=forf)
        else:
            return render_template("utlan.html", error="error")

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