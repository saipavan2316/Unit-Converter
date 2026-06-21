from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/length", methods=["GET", "POST"])
def length():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_length(value, from_unit, to_unit)

    return render_template("length.html", result=result)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_weight(value, from_unit, to_unit)

    return render_template("weight.html", result=result)


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_temperature(value, from_unit, to_unit)

    return render_template("temperature.html", result=result)

def convert_length(value, from_unit, to_unit):
    units = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344
    }

    meters = value * units[from_unit]
    result = meters / units[to_unit]

    return round(result, 6)

def convert_weight(value, from_unit, to_unit):
    units = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "ounce": 28.3495,
        "pound": 453.592
    }

    grams = value * units[from_unit]
    result = grams / units[to_unit]

    return round(result, 6)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15

    # Convert from Celsius to target unit
    if to_unit == "celsius":
        result = celsius
    elif to_unit == "fahrenheit":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        result = celsius + 273.15

    return round(result, 6)



if __name__ == "__main__":
    app.run(debug=True)