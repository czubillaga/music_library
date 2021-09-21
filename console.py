from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist = Artist('Frank Ocean')
album = Album('Blonde', artist, 2016, 'Pop')

artist_repository.save(artist)

album_repository.save(album)
