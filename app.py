from flask import Flask
from temperatures import convert_fahrenheit_to_celsius, convert_celsius_to_fahrenheit

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the Temperature Conversion App/Webpage!"


@app.route('/convert/c_to_f/<float:celsius>')
def convert_c_to_f(celsius):
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f"Temperature: {celsius} Celsius is {fahrenheit:.2f} Fahrenheit."


@app.route("/convert/f_to_c/<float:fahrenheit>")
def convert_f_to_c(fahrenheit):
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    return f"Temperature: {fahrenheit} Fahrenheit is {celsius:.2f} Celsius."


if __name__ == '__main__':
    app.run()
