from flask import request
from app import app
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return{
        "message": "user created",
        "data": "data"
    }