from __future__ import division
import flask
import sys
from tensorflow.keras.preprocessing.text import Tokenizer
import inference as library
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
CORS(app)
model = None
tokenizer = Tokenizer()
# max_sequence_len = None
sys.setrecursionlimit(40000)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return flask.jsonify({
        "status": False,
        "recommendations": [],
        "error": str(e)
    }), code


@app.route("/words_rs_biLSTM", methods=["POST"])
def predict():
    try:
        # initialize the data dictionary that will be returned from the api
        data = {"success": False}
        # ensure an image was properly uploaded to our endpoint
        if flask.request.method == "POST":
            # seed_words = flask.request.args.get('current_frequence')
            # next_words = int(flask.request.args.get('next_words'))
            # num_samples = flask.request.args.get('num_samples')
            request_data = flask.request.json
            # print(request_data)
            seed_words = request_data.get('current_frequence')
            next_words = request_data.get('next_words')
            if seed_words is None or next_words is None:
                raise ValueError("Missing required parameters: seed_words or next_words")
            next_words = int(next_words)
            num_samples = request_data.get('num_samples')

            if num_samples is not None:
                print("zo")
                num_samples = int(num_samples)
                results = library.generate_text(seed_words, next_words, num_samples)
            else:
                print("zo1")
                results = library.predict(seed_words, next_words)
            response = flask.jsonify(results)
            response.headers.add("Access-Control-Allow-Origin", "*")
            print(results)
            return response, 200
    except Exception as e:
        return handle_error(e)


if __name__ == "__main__":
    library.loading_model()
    print(("* Loading  model and Flask starting server..." +
           "please wait until server has fully started"))
    app.run(host='0.0.0.0', port=5555, threaded=True)