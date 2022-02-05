from pymongo import MongoClient
from config.creds import creds

dbUser = creds.get('DB_USER')
dbPassword = creds.get('DB_PASSWORD')
dbName = creds.get('DB_DB_NAME')
colName = creds.get('DB_COL_NAME')

conn = MongoClient(
    f"mongodb+srv://{dbUser}:{dbPassword}@iot-cluster.8fdtu.mongodb.net/{dbName}?retryWrites=true&w=majority")

db = conn["iot-db"]
col = db["iot-collection"]
