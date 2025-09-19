from typing import List
from core.database import get_session
from sqlalchemy import select
from fastapi import Depends, APIRouter, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from compus.models import (
    Campus,
    Building,
    Room,
    RoomItems,
    Request,
)
from compus.schemes import (
    # Campus #
    GetCampus,
    CreateCampus,
    UpdateCampus,
    # Building #
    GetBuilding,
    CreateBuilding,
    UpdateBuilding,
    # Room #
    GetRoom,
    CreateRoom,
    UpdateRoom,
    # RoomItems #
    GetRoomItems,
    CreateRoomItems,
    UpdateRoomItems,
    # Request #
    GetRequest,
    CreateRequest,
    UpdateRequest,
)

router = APIRouter(prefix='/campus', tags=['campus'])
router_for_building = APIRouter(prefix='/building', tags=['building'])
router_for_room = APIRouter(prefix='/room', tags=['room'])
router_for_room_item = APIRouter(prefix='/room_item', tags=['room_item'])
router_for_request = APIRouter(prefix='/request', tags=['request'])


#########################
# campus
#########################
@router.get('/get_campuses', response_model=List[GetCampus])
async def get_campus(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Campus))
    about_uses = result.scalars().all()
    return about_uses


@router.get('/get_campus_by_id/{about_us_id}', response_model=GetCampus)
async def get_campus_by_id(db: AsyncSession = Depends(get_session), about_us_id: int = Path()):
    result = await db.execute(select(Campus).filter(Campus.id == about_us_id))
    campus = result.scalars().first()
    if campus is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Campus not found'
        )
    return campus


@router.post('/create_campus', response_model=GetCampus)
async def create_campus(campus_data: CreateCampus, db: AsyncSession = Depends(get_session)):
    campus = Campus(**campus_data.dict())
    db.add(campus)
    await db.commit()
    await db.refresh(campus)
    return campus


@router.patch('/update_campus/{campus_id}', response_model=GetCampus)
async def update_campus(
        campus_data: UpdateCampus,
        db: AsyncSession = Depends(get_session),
        campus_id: int = Path()):
    query = await db.execute(select(Campus).filter(Campus.id == campus_id))
    campus = query.scalars().first()

    if campus is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Campus not found'
        )

    update_data = campus_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(campus, key, value)

    await db.commit()
    await db.refresh(campus)
    return campus


@router.delete('/delete_campus/{campus_id}')
async def delete_campus(campus_id: int = Path(), db: AsyncSession = Depends(get_session)):
    query = await db.execute(select(Campus).filter(Campus.id == campus_id))
    campus = query.scalars().first()

    if campus is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Campus not found'
        )

    await db.delete(campus)
    await db.commit()
    return {'detail': 'Successfully deleted'}


#########################
# Building
#########################
@router_for_building.get('/get_buildings', response_model=List[GetBuilding])
async def get_buildings(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Building))
    buildings = result.scalars().all()
    return buildings


@router_for_building.get('/get_building_by_id/{building_id}', response_model=GetBuilding)
async def get_building_by_id(db: AsyncSession = Depends(get_session), building_id: int = Path()):
    result = await db.execute(select(Building).filter(Building.id == building_id))
    building = result.scalars().first()
    if building is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Building not found'
        )
    return building


@router_for_building.post('/create_building', response_model=GetBuilding)
async def create_building(building_data: CreateBuilding, db: AsyncSession = Depends(get_session)):
    building = Building(**building_data.dict())
    db.add(building)
    await db.commit()
    await db.refresh(building)
    return building


@router_for_building.patch('/update_building/{building_id}', response_model=GetBuilding)
async def update_buildings(
        building_data: UpdateBuilding,
        db: AsyncSession = Depends(get_session),
        building_id: int = Path()):
    query = await db.execute(select(Building).filter(Building.id == building_id))
    building = query.scalars().first()

    if building is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Building not found'
        )

    update_data = building_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(building, key, value)

    await db.commit()
    await db.refresh(building)
    return building


@router_for_building.delete('/delete_building/{building_id}')
async def delete_buildings(db: AsyncSession = Depends(get_session), building_id: int = Path()):
    query = await db.execute(select(Building).filter(Building.id == building_id))
    building = query.scalars().first()

    if building is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Building not found'
        )

    await db.delete(building)
    await db.commit()
    return {'detail': 'Successfully deleted'}


#########################
# Room
#########################
@router_for_room.get('/get_rooms', response_model=List[GetRoom])
async def get_rooms(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Room))
    rooms = result.scalars().all()
    return rooms


@router_for_room.get('/get_room_by_id/{room_id}', response_model=GetRoom)
async def get_room_by_id(db: AsyncSession = Depends(get_session), room_id: int = Path()):
    result = await db.execute(select(Room).filter(Room.id == room_id))
    room = result.scalars().first()
    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room not found'
        )
    return room


@router_for_room.post('/create_room', response_model=GetRoom)
async def create_room(room_data: CreateRoom, db: AsyncSession = Depends(get_session)):
    room = Room(**room_data.dict())
    db.add(room)
    await db.commit()
    await db.refresh(room)
    return room


@router_for_room.patch('/update_room/{room_id}', response_model=GetRoom)
async def update_room(room_data: UpdateRoom, db: AsyncSession = Depends(get_session), room_id: int = Path()):
    query = await db.execute(select(Room).filter(Room.id == room_id))
    room = query.scalars().first()

    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room not found'
        )

    update_data = room_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(room, key, value)

    await db.commit()
    await db.refresh(room)
    return room


@router_for_room.delete('/delete_room/{room_id}')
async def delete_room(db: AsyncSession = Depends(get_session), room_id: int = Path()):
    query = await db.execute(select(Room).filter(Room.id == room_id))
    room = query.scalars().first()

    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room not found'
        )

    await db.delete(room)
    await db.commit()
    return {'detail': 'Successfully deleted'}


#########################
# RoomItems
#########################
@router_for_room_item.get('/get_room_items', response_model=List[GetRoomItems])
async def get_room_items(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(RoomItems))
    room_items = result.scalars().all()
    return room_items


@router_for_room_item.get('/get_room_item_by_id/{room_item_id}', response_model=GetRoomItems)
async def get_room_item_by_id(db: AsyncSession = Depends(get_session), room_item_id: int = Path()):
    result = await db.execute(select(RoomItems).filter(RoomItems.id == room_item_id))
    room_item = result.scalars().first()
    if room_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room Item not found'
        )
    return room_item


@router_for_room_item.post('/create_room_item', response_model=GetRoomItems)
async def create_room_item(room_item_data: CreateRoomItems, db: AsyncSession = Depends(get_session)):
    room_item = RoomItems(**room_item_data.dict())
    db.add(room_item)
    await db.commit()
    await db.refresh(room_item)
    return room_item


@router_for_room_item.patch('/update_room_item/{room_item_id}', response_model=GetRoomItems)
async def update_room_item(room_item_data: UpdateRoomItems, db: AsyncSession = Depends(get_session), room_item_id: int = Path()):
    query = await db.execute(select(RoomItems).filter(RoomItems.id == room_item_id))
    room_item = query.scalars().first()

    if room_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room Item not found'
        )

    update_data = room_item_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(room_item, key, value)

    await db.commit()
    await db.refresh(room_item)
    return room_item


@router_for_room_item.delete('delete_room_item/{room_item_id}')
async def delete_room_item(db: AsyncSession = Depends(get_session), room_item_id: int = Path()):
    query = await db.execute(select(RoomItems).filter(RoomItems.id == room_item_id))
    room_item = query.scalars().first()

    if room_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Room Item not found'
        )

    await db.delete(room_item)
    await db.commit()
    return {'detail': 'Successfully deleted'}


#########################
# Request
#########################
@router_for_request.get('/get_requests', response_model=List[GetRequest])
async def get_requests(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Request))
    requests = result.scalars().all()
    return requests


@router_for_request.get('/get_request_by_id/{request_id}', response_model=GetRequest)
async def get_request_by_id(db: AsyncSession = Depends(get_session), request_id: int = Path()):
    result = await db.execute(select(Request).filter(Request.id == request_id))
    request = result.scalarbuildingss().first()
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Request not found'
        )
    return request


@router_for_request.post('/create_request', response_model=GetRequest)
async def create_request(request_data: CreateRequest, db: AsyncSession = Depends(get_session)):
    request = Request(**request_data.dict())
    db.add(request)
    await db.commit()
    await db.refresh(request)
    return request


@router_for_request.patch('/update_request/{request_id}', response_model=GetRequest)
async def update_request(request_data: UpdateRequest, db: AsyncSession = Depends(get_session), request_id: int = Path()):
    query = await db.execute(select(Request).filter(Request.id == request_id))
    request = query.scalars().first()

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Request not found'
        )

    update_data = request_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(request, key, value)

    await db.commit()
    await db.refresh(request)
    return request


@router_for_request.delete('/delete_request/{request_id}')
async def delete_request(db: AsyncSession = Depends(get_session), request_id: int = Path()):
    query = await db.execute(select(Request).filter(Request.id == request_id))
    request = query.scalars().first()

    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Request not found'
        )

    await db.delete(request)
    await db.commit()
    return {'detail': 'Successfully deleted'}
