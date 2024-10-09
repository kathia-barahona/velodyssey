from typing import Any

from requests import RequestException

from velodyssey.velodyssey.clients.base_client import BaseClient
from velodyssey.velodyssey.clients.open_route_service.constants import ORSCyclingProfile
from velodyssey.velodyssey.routes.constants import DistanceUnits
from velodyssey.velodyssey.settings import OPEN_ROUTE_SERVICE_API_KEY
from velodyssey.velodyssey.routes.models import CoordinatesModel


class OpenRouteServiceClient(BaseClient):
    API_BASE_URL = "https://api.openrouteservice.org/v2/"
    DIRECTIONS_PATH = "/directions/{profile}/geojson"

    def _get_headers(self) -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Accept": "application/geo+json",
            "Authorization": OPEN_ROUTE_SERVICE_API_KEY,
        }

    def get_directions(
        self,
        waypoints: list[CoordinatesModel],
        profile: ORSCyclingProfile = ORSCyclingProfile.CYCLING_REGULAR,
        units: DistanceUnits = DistanceUnits.KILOMETERS,
    ) -> dict[str, Any]:
        try:
            path = self.DIRECTIONS_PATH.format(profile=profile)
            response = self.post(
                path=path,
                data={
                    "coordinates": [coordinate.to_list() for coordinate in waypoints],
                    "elevation": True,
                    "units": units,
                }
            )
            return response.json()
        except RequestException as e:
            self.logging.error("An error occurred while trying to fetch directions.")
            return {}
