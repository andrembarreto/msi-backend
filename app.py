import asyncio
from flask import Flask, request, jsonify
from werkzeug.exceptions import UnsupportedMediaType

from journey_repository_impl import JourneyRepositoryImpl
from journey_point_repository_impl import JourneyPointRepositoryImpl
from bus_line_repository_impl import BusLineRepositoryImpl
from journey_service_impl import JourneyServiceImpl
from http_adapter import HTTPAdapter, HTTPStatusCode
from database import initialize_database, close_database


def create_app() -> Flask:
    app = Flask(__name__)
    journey_repo = JourneyRepositoryImpl()
    journey_point_repo = JourneyPointRepositoryImpl()
    bus_line_repo = BusLineRepositoryImpl()
    journey_service = JourneyServiceImpl(journey_repo, journey_point_repo, bus_line_repo)
    http_adapter = HTTPAdapter(journey_service)

    @app.post('/receive-mobility-data')
    async def receive_mobility_data():
        try:
            data = request.json
        except UnsupportedMediaType:
            return jsonify({'status': HTTPStatusCode.BAD_FORMAT})

        return http_adapter.receive_mobility_data(data)

    return app


def main():
    initialize_database()
    app = create_app()
    asyncio.run(app.run(host='0.0.0.0', debug=True))
    close_database()


if __name__ == "__main__":
    main()
