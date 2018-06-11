from flask import request, jsonify, Flask
from flask_cors import CORS
from ..main import validate_uid

# FlaskAPI does not support flask_graphql, using Flask instead
app = Flask(__name__)
cors = CORS(app)


@app.route("/validate_uid", methods=['POST'])
def api_validate_uid():
  """ Add vertex templates """
  success, uid = validate_uid(request.json["fingerprint"])
  return jsonify({"success": success, "uid": uid})


if __name__ == "__main__":
  print('Flask app running at 0.0.0.0:8891')
  app.run(host='0.0.0.0', port=8891)

