import asyncio
from flask import Flask, request, jsonify
from db import MobilityDataBaseController

app = Flask(__name__)

db_controller = MobilityDataBaseController()

@app.route("/receive-mobility-data", methods=["POST"])
async def receive_json():
    try:
        data = request.json
    except Exception as e:
        error_message = {"message": repr(e)}
        return jsonify(error_message)

    db_controller.store_journey_entries(data)

    confirmation = {"message": "Mobility data received successfully"}
    return jsonify(confirmation)


if __name__ == "__main__":
    asyncio.run(app.run(debug=True))
