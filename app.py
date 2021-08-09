from flask import Flask, render_template, make_response, jsonify

# App config.
DEBUG = True
app = Flask(__name__, template_folder='./templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", version="1.0.0")


@app.route('/api', methods=['GET'])
def api_test():
    return make_response("success")

