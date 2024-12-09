from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def box():
    return render_template("index.html")

@app.route("/4")
def box_4():
    return render_template("index1.html")

@app.route("/<int:x>/<int:y>")
def box_x_y(x,y):
    return render_template("index2.html", x=x, y=y)

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def box_x_y_c(x,y,color1, color2):
    return render_template("index3.html", x=x, y=y, color1=color1, color2=color2)




if __name__ == "__main__":
    app.run(debug=True)

