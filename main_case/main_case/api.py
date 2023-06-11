from ninja import NinjaAPI
from testov.clear_api import router

api = NinjaAPI()

api.add_router("", router)