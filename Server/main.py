from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse, Response, FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from database.addDataDatabase import addSongs
from fastapi.encoders import jsonable_encoder 
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')#Information
client = AsyncIOMotorClient(MONGO_URI)
db = client["spotify"]
songs_collection = db["songs"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  #FrontEnd Origin
    allow_credentials=True,
    allow_methods=["*"],  #Allows all methods
    allow_headers=["*"],  
)


Chunk_Size = 1024 * 1024

@app.get("/stream/{title}")#Retrieves a song per chunk from database
async def streamSong(title: str, request: Request):#Gets the title and the request

    song = await songs_collection.find_one({"title": title})#Searches for a song, but if not found return error
    if not song:#
        raise HTTPException(status_code=404, detail="Song not found")
    file_path = song["file_path"]#Get the filepath

    if not os.path.exists(file_path):#If the file its not found...
        raise HTTPException(status_code=404, detail="Archivo de audio no encontrado")

    file_size = os.path.getsize(file_path)#Gets the size of the file
    range_header = request.headers.get("range")#Setting a range from the client
    
    if range_header:#If the user sets a range, get from there
        start = int(range_header.replace("bytes=","").split("-")[0])
    else:#Else get from 0
        start = 0
    
    end = min(start + Chunk_Size, file_size - 1)#Calculate the final length of how much send
    content_length = end - start + 1#Gets the real bytes to send

    def iterfile(path, start_byte, end_byte):
        with open(file_path, mode="rb") as f:#Opens the file
            f.seek(start_byte)#Goes to the initial byte(Calculated)
            remaining = end_byte - start_byte + 1
            while remaining > 1:
                chunk_size = min(8192, remaining)#Reads in blocks of 8kb
                data = f.read(chunk_size)
                if not data:
                    break
                yield data
                remaining -= len(data)#Reduce the remaining size, tills its less than 1 
    headers = {
        "Content-Range": f"bytes {start}-{end}/{file_size}",#What part of the file im sending
        "Accept-Ranges": "bytes",#Tells the browser to accept range requests
        "Content-Length": str(content_length),#How many bytes
        "Content-Type": "audio/mpeg"#Type of file -> mp3
    }
            
    return StreamingResponse(
        iterfile(file_path,start, end),
        status_code=206 if range_header else 200,# 206 means partial content, 200 complete file ok
        headers = headers
    )

@app.get("/")#Root
def salute():
    return "Hollaaa"

@app.get("/songs")
async def getSongList():#Get all the songs information
    songs = await songs_collection.find().to_list()
    if not songs:
        print("No encontre canciones" , songs[0])
        return HTTPException(status_code=404, detail='No Songs found')
    for song in songs:
        song["_id"] = str(song["_id"])
    return jsonable_encoder(songs)

@app.post("/hardcode")#Hardcoe values to the database
def harcode():
    addSongs()
    return{"state":"Users added"}

@app.get("/image")
async def get_image(img_path: str):
    if not os.path.exists(img_path):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

    return FileResponse(path=img_path, media_type="image/jpeg")

@app.get("/image/{title}")
async def get_image_withSong(title: str):
    song = await songs_collection.find_one({"title": title})
    if not song or not os.path.exists(song["img_path"]):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

    return FileResponse(path=song["img_path"], media_type="image/jpeg")
