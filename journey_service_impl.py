from typing import Any

from journey_service import JourneyService


class JourneyServiceImpl(JourneyService):
    def register_journey(self, journey_data: list[dict[str, Any]]) -> None:
        ...

