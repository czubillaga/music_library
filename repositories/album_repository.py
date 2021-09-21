from db.run_sql import run_sql
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, artist, year, genre) VALUES (%s,%s,%s, %s) RETURNING *"
    values = [album.title, album.artist.name, album.year, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

