class Record:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
       

    def get_title(self):
        return self.title.title()
    
    def get_year(self):
        return self.year
    
    def get_name(self):
        return self.artist
    
    def get_songs(self):
        return self.songs
    
    def get_artist(self):
        return self.artist
    
    def total_runtime(self):
        total_run = 0
        for item in self.songs:
            total_run += item.runtime
        return total_run
    
    def has_song(self, song):
        if song in self.songs:
            return True
        else:
            return False
    
    def get_longest_song(self):
        return max(self.runtime)
        
