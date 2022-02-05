def deviceEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "type": item["type"],
        "data": item["data"],
        "soc": item["soc"],
        "location": item["location"],
        "brand": item["brand"],
        "mac": item["mac"]
    }


def devicesEntity(entity) -> list:
    return [deviceEntity(item) for item in entity]
