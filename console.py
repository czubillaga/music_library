from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Frank Ocean')
artist_repository.save(artist1)
artist2 = Artist('The Beatles')
artist_repository.save(artist2)

album1 = Album('Blonde', artist1, 2016, 'Pop')
album2 = Album('Endless', artist1, 2016, 'Pop')
album3 = Album('Revolver',artist2, 1965, 'Rock')



album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)

# albums = album_repository.select_all()
# for album in albums:
#     print(album.__dict__)

artist1.name = "Christopher Breaux"
artist_repository.update(artist1)

album3.year = 1966
album_repository.update(album3)
