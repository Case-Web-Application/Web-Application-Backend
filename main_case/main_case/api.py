from ninja import NinjaAPI
from testov.api import router

api = NinjaAPI()

api.add_router("", router)