from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    data = request.form
    option = data["options"]
    print(f'getting the data: {option}')

    return render_template("result.html", option=option)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
