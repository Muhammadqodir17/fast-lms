from pydantic import BaseModel, validator
from typing import Optional, List
from compus.models import BuildingTip
from datetime import date


##########################
# Campus
##########################
class GetCampus(BaseModel):
    id: int
    name: str
    address: str

    model_config = dict(from_attributes=True)


class CreateCampus(BaseModel):
    name: str
    address: str


class UpdateCampus(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


##########################
# Building
##########################
class GetBuilding(BaseModel):
    id: int
    campus_id: int
    tip: BuildingTip
    floors: int

    model_config = dict(from_attributes=True)


class CreateBuilding(BaseModel):
    campus_id: int
    tip: BuildingTip
    floors: int


class UpdateBuilding(BaseModel):
    campus_id: Optional[int] = None
    tip: Optional[BuildingTip] = None
    floors: Optional[int] = None


##########################
# Room
##########################
class GetRoom(BaseModel):
    id: int
    building_id: int
    name: str
    floor: int

    model_config = dict(from_attributes=True)


class CreateRoom(BaseModel):
    building_id: int
    name: str
    floor: int


class UpdateRoom(BaseModel):
    building_id: Optional[int] = None
    name: Optional[str] = None
    floor: Optional[int] = None


##########################
# RoomItems
##########################
class GetRoomItems(BaseModel):
    id: int
    request_id: Optional[int] = None
    room_id: int
    name: str
    quantity: int
    data: date
    status: bool

    model_config = dict(from_attributes=True)


class CreateRoomItems(BaseModel):
    request_id: Optional[int] = None
    room_id: int
    name: str
    quantity: int
    data: date
    status: bool

    @validator("request_id")
    def validate_request_id(cls, v):
        if v == 0:
            return None
        return v


class UpdateRoomItems(BaseModel):
    request_id: Optional[int] = None
    room_id: Optional[int] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    data: Optional[date] = None
    status: Optional[bool] = None


##########################
# Request
##########################
class GetRequest(BaseModel):
    id: int
    user_id: int
    room_id: int

    model_config = dict(from_attributes=True)


class CreateRequest(BaseModel):
    user_id: int
    room_id: int


class UpdateRequest(BaseModel):
    user_id: Optional[int] = None
    room_id: Optional[int] = None


#############################################
##
#############################################
class BuildingByFloorData(BaseModel):
    building_id: int
    floor: int


class BuildingRoomItemForBuildingGet(BaseModel):
    id: int
    name: str
    data: Optional[date]
    quantity: int
    status: bool

    model_config = dict(from_attributes=True)


class GetBuildingRoom(BaseModel):
    id: int
    name: str
    room_items: List[BuildingRoomItemForBuildingGet] = []

    model_config = dict(from_attributes=True)


class GetBuildingResponse(BaseModel):
    id: int
    tip: Optional[str] = None
    floors: int | None
    total_rooms: int
    rooms: List[GetBuildingRoom] = []

    model_config = dict(from_attributes=True)


class GetBuildingByRoomResponse(BaseModel):
    room: GetRoom
    room_items: Optional[List[GetRoomItems]] = []
    building: GetBuilding
    campus: GetBuildingRoom

    model_config = dict(from_attributes=True)