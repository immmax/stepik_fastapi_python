import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {"Answer": "Returned by server"}


@api.get("/")
def index():
    return response


@api.get("/welcome")
def welcome():
    return "Welcome page"


@api.get("/about")
def about():
    return "About page"
