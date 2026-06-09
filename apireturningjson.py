from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API"})

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id":1, "name": "pralad"},
        {"id":2, "name": "john"},
        {"id":3, "name": "raj"},
        {"id":4, "name": "james"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)