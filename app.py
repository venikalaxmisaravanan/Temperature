from flask import Flask, request, jsonify

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


@app.route("/")
def home():
    return "Temperature Converter"


@app.route("/convert")
def convert():
    conversion_type = request.args.get("type")
    value = request.args.get("value")

    if value is None:
        return jsonify({"error": "Temperature value is required"}), 400

    try:
        temperature = float(value)
    except ValueError:
        return jsonify({"error": "Temperature must be a number"}), 400

    if conversion_type == "c_to_f":
        result = celsius_to_fahrenheit(temperature)
    elif conversion_type == "f_to_c":
        result = fahrenheit_to_celsius(temperature)
    else:
        return jsonify({"error": "Invalid conversion type"}), 400

    return jsonify({"result": round(result, 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)