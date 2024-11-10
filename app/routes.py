from flask import Blueprint, jsonify, request
from io import BytesIO
from json import loads
import requests, socket

main = Blueprint('main', __name__)

@main.route("/<route>")
def send_request_data(route : str):
    request_data = {
        "route": route,
        "ip": request.remote_addr,
        "status": 200
    }
    requests.post(url="http://127.0.0.1:4001/api/sample" ,json=request_data)
    return jsonify(request_data)