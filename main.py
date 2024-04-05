from flask import Flask


app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome"


@app.route("/name/<int:id>/<some_name>")
def name(id, some_name):
    return f"Ник: {some_name}. ID: {id}"


@app.route("/age/<int:age>")
def print_age(age):
    if age < 18:
        return "Вы несовершеннолетний"
    else:
        return "Доступ получен"


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
    )
