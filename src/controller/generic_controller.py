from flask import Blueprint, jsonify
import json
import os

generic_controller = Blueprint('generic_controller', __name__)

@generic_controller.route('/swagger.json')
def swagger():
    current_dir = os.path.dirname(__file__)
    swagger_file_path = os.path.join(current_dir, '..', '..', 'docs', 'swagger.json')

    swagger_file_path = os.path.abspath(swagger_file_path)

    with open(swagger_file_path, 'r') as f:
        return jsonify(json.load(f))

@generic_controller.route('/health')
def health_check():
    return jsonify({"status": "UP"}), 200
