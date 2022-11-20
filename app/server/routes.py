import time
from aiohttp import web
from app import user_dict
from app import StartTime
from app.utils.time_format import get_readable_time

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"status": "running",
                              "uptime": get_readable_time(time.time() - StartTime),
                              "bot_username": '@'+user_dict.username})
