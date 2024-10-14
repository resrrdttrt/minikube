# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# API 1: GET /hello
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# API 2: POST /echo
@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

# API 3: GET /sum?a=<int>&b=<int>
@app.route('/sum', methods=['GET'])
def sum_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        return jsonify({"error": "Please provide two integers 'a' and 'b' in the query string."}), 400
    return jsonify({"sum": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
