from pydantic import BaseModel
from typing import Optional
from compus.models import BuildingTip
from datetime import date


##########################
# Campus
##########################
class GetCampus(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


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
    request_id: int
    room_id: int
    name: str
    quantity: int
    data: date
    status: bool

    class Config:
        orm_mode = True


class CreateRoomItems(BaseModel):
    request_id: int
    room_id: int
    name: str
    quantity: int
    data: date
    status: bool


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

    class Config:
        orm_mode = True


class CreateRequest(BaseModel):
    user_id: int
    room_id: int


class UpdateRequest(BaseModel):
    user_id: Optional[int] = None
    room_id: Optional[int] = None

