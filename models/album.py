class Album: 

    def __init__(self, title, artist, year, genre, id=None):
        self.title = title
        self.artist = artist
        self.artist_name = artist.name
        self.year = year
        self.genre = genre
        self.id = id