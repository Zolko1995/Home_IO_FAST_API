import imp
from fastapi import APIRouter

from models.device import Device
from config.db import conn
from schemas.device import deviceEntity, devicesEntity
from bson import ObjectId

device = APIRouter()


@device.get("/")
async def find_all_devices():
    print(conn.db.col.find())
    return devicesEntity(conn.db.col.find())


@device.get("/{id}")
async def find_device(id):
    print(conn.db.col.find())
    return deviceEntity(conn.db.col.find_one({"_id": ObjectId(id)}))


@device.post("/")
async def create_device(device: Device):
    conn.db.col.insert_one(dict(device))
    return devicesEntity(conn.db.col.find())


@device.put("/{id}")
async def update_device(id, device: Device):
    conn.db.col.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(device)})
    return deviceEntity(conn.db.col.find_one({"_id": ObjectId(id)}))


@device.delete("/{id}")
async def delete_device(id, device: Device):
    return deviceEntity(conn.db.col.find_one_and_delete({"_id": ObjectId(id)}))
