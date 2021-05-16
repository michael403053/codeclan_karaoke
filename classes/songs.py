class Songs:
    def __init__(self):
        self.song_selection = []
        self.songs_to_add = []
        self.songs_list = [
        #0
        "Castles in the Sky",
        #1
        "Angel Of Death",
        #2
        "The Real Slim Shady",
        #3
        "Didn't I",
        #4
        "Baltimore",
        #5
        "Hey Jude",
        #6
        "This is America",
        #7
        "That's Not Me",
        #8
        "Tequila"
        ]
    

    def song_list(self):
        return self.songs_list

    def song_list_length(self):
        return len(self.songs_list)

    def song_selection_length(self):
        return len(self.song_selection)

    def add_song_to_selection(self):
        self.songs_to_add.extend([self.songs_list[0], self.songs_list[2], self.songs_list[3], self.songs_list[5]])
        self.song_selection = self.songs_to_add
        return self.song_selection

    def clear_song_selection(self):
        self.song_selection = []
        return self.song_selection

    def song_selection_list(self):
        return self.song_selection
        

        
        