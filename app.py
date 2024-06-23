import flask
from Api.user_controller import user_controller


app = flask.Flask(__name__)

app.register_blueprint(user_controller)

@app.route('/', methods=['GET'])
def index():
    return "Hello"

app.run("0.0.0.0", port=5000, debug=True)