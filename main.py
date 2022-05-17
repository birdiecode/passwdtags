import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

@app.route('/v1/tags')
def hello_world():
    return json.dumps([{"label": "Coffee"+str(w), "id": w, "status": False} for w in range(0,11)])

if __name__ == '__main__':
    app.run()

