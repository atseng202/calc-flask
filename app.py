# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operator_mappings = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/math/<operator>")
def manipulate_nums(operator):
    """ Handles addition of a and b from query params """
    if operator not in operator_mappings:
        return "<h1>NOT VALID OPERATION</h1>"

    a = request.args["a"]
    b = request.args["b"]

    return f"{operator_mappings[operator](int(a), int(b))}"
