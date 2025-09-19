from fastapi import FastAPI
from compus.views import router as campus_router
from compus.views import router_for_building as router_for_building
from compus.views import router_for_room as router_for_room
from compus.views import router_for_room_item as router_for_room_item
from compus.views import router_for_request as router_for_request

app = FastAPI()

app.include_router(campus_router)
app.include_router(router_for_building)
app.include_router(router_for_room)
app.include_router(router_for_room_item)
app.include_router(router_for_request)