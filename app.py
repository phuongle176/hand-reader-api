from flask import Flask, request, jsonify
from process import analyze_hand

app = Flask(__name__)

@app.route("/")
def home():
    return "Palm Reading API is running."

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded."}), 400

    image_file = request.files["image"]
    description = analyze_hand(image_file)
    return jsonify({"description": description})
