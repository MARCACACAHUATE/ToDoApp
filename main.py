from flask import render_template

from app import create_app

app, db = create_app()

from models.users import User

todos = ["Caca", "Pipi", "Popo"]

@app.route("/", methods = ['POST', 'GET'])
def home():
    context = {
        "todos": todos
    }

    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(port = 5000, debug = True)