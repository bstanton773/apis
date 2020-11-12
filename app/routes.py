from app import app
from flask import jsonify
from app.models import User


@app.route('/')
def index():
    data = {
        'users': [user.to_dict() for user in User.query.all()]
    }
    return jsonify(data)
