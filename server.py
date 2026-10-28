from flask import Flask, jsonify
import os

app = Flask(__name__)

port = os.getenv("PORT", 3203)
# /var/local/emhttp from the Unraid host, mounted read-only
emhttp_dir = os.getenv("EMHTTP_DIR", "/emhttp")
allowed_files = [f.strip() for f in os.getenv("ALLOWED_FILES", "disks.ini").split(",")]


# same output as PHP's parse_ini_file($path, true) for emhttp's ["section"] / key="value" files
def parse_ini(path):
    data = {}
    section = data
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("["):
                section = data.setdefault(line[1:-1].strip('"'), {})
            elif "=" in line:
                key, value = line.split("=", 1)
                section[key.strip()] = value.strip().strip('"')
    return data


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(ok=True)


@app.route('/<path:path>', methods=['GET'])
def catch_all(path):
    if path not in allowed_files:
        response = jsonify(error="Not Found")
        response.status_code = 404
        return response

    try:
        return jsonify(ok=True, data=parse_ini(os.path.join(emhttp_dir, path)))

    except Exception as error:
        print(error, flush=True)
        response = jsonify(error="Internal Server Error")
        response.status_code = 500
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
