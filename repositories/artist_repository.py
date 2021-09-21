from db.run_sql import run_sql

from models.artist import Artist

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        artist = Artist(results['name'])

    return artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

