from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Karthikeyan G"


@app.route("/22it017")
def register_number():
    return "22IT017"

@app.route("/IT")
def department():
    return "IT(Information Technology)"

if __name__ == "__main__":
    app.run(debug=True)
