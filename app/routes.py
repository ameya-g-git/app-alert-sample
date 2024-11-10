from flask import Blueprint, jsonify, request
from io import BytesIO
from json import loads
import requests, socket

main = Blueprint('main', __name__)

@main.route("/<route>", methods=['GET', 'POST'])
def send_request_data(route : str):
    request_data = {
        "ip": request.remote_addr,
        "endpoint": route,
        "method": request.method
    }
    requests.post(url="http://127.0.0.1:4001/traffic" ,json=request_data)
    return jsonify(request_data)