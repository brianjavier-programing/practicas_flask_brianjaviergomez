from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    area = None
    perimetro = None

    if request.method == "POST":
        lado = float(request.form["lado"])

        area = lado * lado
        perimetro = lado * 4

    return render_template(
        "cuadrado.html",
        area=area,
        perimetro=perimetro
    )

if __name__ == "__main__":
    app.run(debug=True)
