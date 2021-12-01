from app import create_app

app = create_app()


@app.route("/")
def home():
    return "Que onda pinches perros"


if __name__ == "__main__":
    app.run(port = 5000, debug = True)