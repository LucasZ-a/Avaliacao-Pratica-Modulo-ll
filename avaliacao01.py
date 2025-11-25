from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/somar", methods = ["get"])
def somar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    soma = valor1+valor2
    return jsonify({"soma":soma})

@app.route("/subtrair", methods=["GET"])
def subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 - valor2
    return jsonify({"subtracao": resultado})


@app.route("/multiplicar", methods=["GET"])
def multiplicar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 * valor2
    return jsonify({"multiplicacao": resultado})


@app.route("/dividir", methods=["GET"])
def dividir():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))

    if valor2 == 0:
        return jsonify({"erro": "Divisão por zero não é permitida"})

    resultado = valor1 / valor2
    return jsonify({"divisao": resultado})

if __name__ == "__main__":
    app.run(debug=True)
