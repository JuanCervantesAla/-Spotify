from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://superemiliano:1234@localhost:27017/spotify?authSource=admin"
client = AsyncIOMotorClient(MONGO_URI)
db = client["spotify"]

songs_collection = db["songs"]