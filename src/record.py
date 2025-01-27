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
        longest_song = 0
        longest_song_index = 0
        for x, song in enumerate(self.songs):
            if longest_song <= song.runtime:
                longest_song = song.runtime
                longest_song_index = x
            return self.songs[longest_song_index]
        
        """
        class Record:
    def __init__(self, title, artist, year):
        self.title = title.title()
        self.artist = artist
        self.year = year
        self.songs = []
    
    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_year(self):
        return self.year
    
    def get_songs(self):
        return self.songs
    
    def total_runtime(self):
        # total_run = 0
        # for song in self.songs:
        #     total_run += song.runtime
        # return total_run
        return sum([song.runtime for song in self.songs])

    def has_song(self, song):
        return song in self.songs
    
    def get_longest_song(self):
        longest = self.songs[0]
        for song in self.songs:
            if song.runtime > longest.runtime:
                longest = song
        return longest
        """

    
        
