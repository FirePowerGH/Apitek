from flask import Flask, jsonify, render_template, request

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
            return "biblio"
        else:
            return "wrong password"
    else:
        return "Hei, Verden"

if __name__ == "__main__":
    app.run(debug=True)