from core.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy import Enum as SqlEnum


class BuildingTip(str, Enum):
    dorm = 'Yotoqxona'
    lab = 'Labaratoriya'
    sport = 'Sportzal'
    library = 'Kutubxona'


class Campus(BaseModel):
    __tablename__ = 'campuses'

    name = Column(String(250))
    address = Column(String(250))

    buildings = relationship('Building', back_populates='campus')

    def __repr__(self):
        return f'<Campus {self.name}>'


class Building(BaseModel):
    __tablename__ = 'buildings'

    campus_id = Column(Integer, ForeignKey('campuses.id'))
    tip = Column(SqlEnum(BuildingTip), nullable=True)
    floors = Column(Integer)

    campus = relationship('Campus', back_populates='buildings')
    rooms = relationship('Room', back_populates='building')

    def __repr__(self):
        return f'<Building {self.name}>'


class Room(BaseModel):
    __tablename__ = 'rooms'

    building_id = Column(Integer, ForeignKey('buildings.id'))
    name = Column(String(250))
    floor = Column(Integer)

    building = relationship('Building', back_populates='rooms')
    room_items = relationship('RoomItems', back_populates='room')
    requests = relationship('Request', back_populates='room')

    def __repr__(self):
        return f'<Room {self.name}>'


class RoomItems(BaseModel):
    __tablename__ = 'room_items'

    request_id = Column(Integer, ForeignKey('requests.id'), nullable=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    name = Column(String(250))
    quantity = Column(Integer, default=0)
    data = Column(Date)
    status = Column(Boolean, default=False)

    room = relationship('Room', back_populates='room_items')
    request = relationship('Request', back_populates='room_items')

    def __repr__(self):
        return f'<Item {self.name}>'


class Request(BaseModel):
    __tablename__ = 'requests'

    user_id = Column(Integer)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    room = relationship('Room', back_populates='requests')
    room_items = relationship('RoomItems', back_populates='request')

    def __repr__(self):
        return f'<Room {self.room_id}'
