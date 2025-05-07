from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://superemiliano:1234@localhost:27017/spotify?authSource=admin")
db = client["spotify"]

def addSongs():
    db.songs.insert_many([
        {"song_id": "1", "title": "Espresso", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/espresso.mp3", "img_path":"songs/espresso.jpeg" , "duration":153},
        {"song_id": "2", "title": "Feather", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/feather.mp3","img_path":"songs/feather.jpeg","duration":153},
        {"song_id": "3", "title": "Juno", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/juno.mp3","img_path":"songs/juno.jpeg","duration":153},
        {"song_id": "4", "title": "Cant read your mind", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/cant.mp3","img_path":"songs/cant.jpeg","duration":153},
        {"song_id": "5", "title": "Busy woman", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/busy_woman.mp3","img_path":"songs/busy_woman.jpeg","duration":153},
        {"song_id": "6", "title": "15 minutes", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/15_minutes.mp3","img_path":"songs/15_minutes.jpeg","duration":153},
        {"song_id": "7", "title": "Cupid", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/cupid.mp3","img_path":"songs/cupid.jpeg","duration":153},
        {"song_id": "8", "title": "Taste", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/taste.mp3","img_path":"songs/taste.jpeg","duration":153},
        {"song_id": "9", "title": "Bed Chem", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/bed_chem.mp3","img_path":"songs/bed_chem.jpeg","duration":153},
        {"song_id": "10", "title": "Good graces", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/good_graces.mp3","img_path":"songs/good_graces.jpeg","duration":153},
        {"song_id": "11", "title": "Nonsense", "artist": "Sabrina Carpenter","plays":98457823, "file_path":"songs/nonsense.mp3","img_path":"songs/nonsense.jpeg","duration":153},
    ])