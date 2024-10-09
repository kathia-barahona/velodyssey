from dataclasses import dataclass

from velodyssey.velodyssey.clients.open_route_service.client import OpenRouteServiceClient
from velodyssey.velodyssey.clients.open_route_service.constants import ORSCyclingProfile
from velodyssey.velodyssey.routes.models import CoordinatesModel, RouteModel
from velodyssey.velodyssey.routes.utils import generate_random_route_name


@dataclass
class RoutePlanner:
    ors_client: OpenRouteServiceClient

    def plan_route(
        self,
        waypoints: list[CoordinatesModel],
        cycling_type: ORSCyclingProfile = ORSCyclingProfile.CYCLING_REGULAR,
        name: str = "",
    ) -> RouteModel:
        name = name or generate_random_route_name()
        route_directions = self.ors_client.get_directions(waypoints=waypoints, profile=cycling_type)
        return RouteModel(name=name, segments=[])
