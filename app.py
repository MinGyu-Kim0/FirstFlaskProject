from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in..."
    else:
        return "Login Form"

if __name__ == '__main__':
    app.run(debug=True)
