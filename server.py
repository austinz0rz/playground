from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "Turn back, friend. There's nothing to see here."

@app.route("/play")

@app.route("/play/<int:number>")
def how_many_squares(number = 3):
    return render_template("index.html", number = number)

@app.route("/play/<int:number>/<color>")
def what_color(number, color):
    return render_template("index.html", color = color, number = number)

if __name__ == "__main__":
    app.run(debug=True)