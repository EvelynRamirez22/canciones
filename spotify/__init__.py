from flask import Flask, send_file

app = Flask(__name__)

with app.app_context():
    from db import init_app
    init_app(app)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/')
def hello():
    return 'Hello, World!'