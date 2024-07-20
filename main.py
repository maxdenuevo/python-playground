from flask import Flask, request, jsonify
import jwt
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    email = body.get('email')
    password = body.get('password')
    if email == 'admin@gmail.com' and password == '123':
        firma = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        return jsonify({ "firma": firma })
    else:
        return "Credenciales invalidas", 401

@app.route('/protected', methods=['POST'])
def protected():
    headers = request.headers
    firma = headers.get('Authorization')
    jwt.decode(firma, "secret", algorithms=["HS256"])
    return "Tienes acceso"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)