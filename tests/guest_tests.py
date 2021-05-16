import unittest
from classes.rooms import Rooms
from classes.guests import Guests

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.rooms = Rooms(5, 10)
        self.guests = Guests()

    def test_guests_can_be_added_to_guest_list(self):
        self.guests.add_guest_to_guests_guest_list()
        self.assertEqual(3, self.guests.guest_list_length())

    def test_more_guests_can_be_added_to_guest_list(self):
        self.guests.add_more_people_to_guest_list()
        self.assertEqual(8, self.guests.guest_list_length())

    