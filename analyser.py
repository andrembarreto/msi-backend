import asyncio
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receive-mobility-data", methods=["POST"])
async def receive_json():
    # Wait for the JSON data to be received
    try:
        data = request.json
    except Exception as e:
        error_message = {"message": repr(e)}
        return jsonify(error_message)

    # Send a confirmation response
    print(data)
    confirmation = {"message": "Mobility data received successfully"}
    return jsonify(confirmation)

if __name__ == "__main__":
    asyncio.run(app.run(debug=True))
