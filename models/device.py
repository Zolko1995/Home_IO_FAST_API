from pydantic import BaseModel

class Device(BaseModel):
    name: str
    type: str
    data: object
    soc: int
    location: str
    brand: str
    mac: str

    
