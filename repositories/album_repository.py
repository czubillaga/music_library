from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, artist, year, genre, artist_id) VALUES (%s,%s,%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.name, album.year, album.genre, album.artist.id]
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
        album = Album(row['title'], artist, row['year'], row['genre'])
        albums.append(album)
    return albums

def select(id):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id=%s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['year'], row['genre'])
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE * FROM albums WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title, artist, year, genre) = (%s,%s,%s,%s) WHERE id=%s"
    values = [album.title, album.artist.name, album.year, album.genre, album.id]
    run_sql(sql, values)