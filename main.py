from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Location(BaseModel):
    latitude: float
    longitude: float


latest_location = None


@app.get("/")
def home():
    return {
        "message": "DreamRAT Backend is running"
    }


@app.post("/location")
def receive_location(location: Location):
    global latest_location

    latest_location = location

    return {
        "message": "Location received successfully",
        "latitude": location.latitude,
        "longitude": location.longitude
    }


@app.get("/location")
def get_location():
    if latest_location is None:
        return {
            "message": "No location received yet"
        }

    return {
        "latitude": latest_location.latitude,
        "longitude": latest_location.longitude
    }