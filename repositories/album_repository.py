from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, artist, year, genre) VALUES (%s,%s,%s, %s) RETURNING *"
    values = [album.title, album.artist.name, album.year, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(results['title'], artist, results['year'], results['genre'])
        albums.append(album)
    return albums