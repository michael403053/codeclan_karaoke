import unittest
from classes.guests import Guests
from classes.rooms import Rooms
from classes.songs import Songs

class TestSong(unittest.TestCase):
    def setUp(self):
        self.songs = Songs()

    def test_song_can_be_returned_from_index_number(self):
        self.assertEqual("Castles in the Sky", self.songs.song_list()[0])

    def test_song_can_be_added_to_song_selection_list(self):
        self.songs.add_song_to_selection()
        self.assertEqual(4, self.songs.song_selection_length())

    def test_song_selection_can_be_cleared(self):
        self.songs.add_song_to_selection()
        self.songs.clear_song_selection()
        self.assertEqual(0, self.songs.song_selection_length())
    

