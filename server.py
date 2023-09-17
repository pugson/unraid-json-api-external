from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

port = os.getenv("PORT", 3203)
server = os.getenv("SERVER", "localhost")


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(ok=True)


@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    try:
        query = path
        unraid_api_url = f"http://{server}/plugins/jsonapi/api.php?file={query}"
        response = requests.get(unraid_api_url).json()

        return jsonify(ok=True, data=response)

    except Exception as error:
        print(error)
        response = jsonify(error="Internal Server Error")
        response.status_code = 500
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)