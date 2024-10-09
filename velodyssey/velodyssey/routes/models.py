from typing import Self

from pydantic import BaseModel


class CoordinatesModel(BaseModel):
    latitude: float
    longitude: float

    def to_list(self) -> list[float]:
        return [self.latitude, self.longitude]

    def to_string(self) -> str:
        return f"{self.latitude},{self.longitude}"

    @classmethod
    def from_list(cls, coordinates: list[float]) -> Self:
        return cls(latitude=coordinates[0], longitude=coordinates[1])


class SegmentModel(BaseModel):
    name: str
    coordinates: list[CoordinatesModel]


class RouteModel(BaseModel):
    id: int | None = None
    name: str
    segments: list[SegmentModel]