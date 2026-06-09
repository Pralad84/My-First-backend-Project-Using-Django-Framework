from flask import Flask, jsonify, request
app =  Flask(__name__)

# Home route

@app.route('/')
def home():
    return "Hello Backend!"

# Get Users

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id":1, "name": "pralad"},
        {"id":2, "name": "john"},
        {"id":3, "name": "raj"},
        {"id":4, "name": "james"}
    ]
    return jsonify(users)

# POST users

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return{
        "message": "user created",
        "data": "data"
    }
if __name__== '__main__':
    app.run(debug=True)