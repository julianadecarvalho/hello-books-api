from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route ('/hello-world', methods = ["GET"])  
def get_hello_world():
    my_resposne = "Hey Y'all!"
    return my_resposne

@hello_world_bp.route('/hello-world/JSON', methods = ["GET"])
def hello_world_json():
    return {
        "name": "CloudCityDev!",
        "message": "Hey Y'all!",
        "hobbies": ["Coding", "Skiing", "Fishing"],
    }, 201

