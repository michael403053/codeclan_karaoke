from classes.songs import Songs
from classes.guests import Guests
from classes.bar import Bar

class Rooms:
    def __init__(self, capacity, entry_fee):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.room_guest_list = []
        self.room_songs_list = []
        self.songs = Songs() 
        self.guests = Guests()
        self.bar = Bar()
        self.admin = {
            'total_cash_in': 0,
            'total_cash_out': 0,       
        }       
        
    def room_song_list_length(self):
        return len(self.room_songs_list)

    def load_song_selection(self):
        self.songs.add_song_to_selection()

        self.room_songs_list = self.songs.song_selection
        return self.room_songs_list
        
    def room_guest_list_length(self):
        return len(self.room_guest_list)

    def load_guest_list(self):
        self.guests.add_guest_to_guests_guest_list()
        self.room_guest_list = self.guests.guests_guest_list
        return self.room_guest_list

    def load_more_guests(self):
        self.guests.add_more_people_to_guest_list()
        self.room_guest_list = self.guests.guests_guest_list
        return self.room_guest_list

    def load_more_guests_with_entry_condition(self):
        self.guests.add_more_people_to_guest_list()
        for person in self.guests.guests_guest_list:
            if person['money'] < self.entry_fee:
                self.guests.guests_guest_list.remove(person)
        self.room_guest_list = self.guests.guests_guest_list
        return self.room_guest_list


    def clear_guest_list(self):
        self.room_guest_list = []
        return self.room_guest_list

    def take_entry_fee_from_guests(self):
        self.load_guest_list()
        for person in self.room_guest_list:
            person['money'] = person['money'] - self.entry_fee
        
    def add_entry_fee_to_admin(self):
        self.load_guest_list()  
        self.admin['total_cash_in'] = self.admin['total_cash_in'] + (self.room_guest_list_length() * self.entry_fee)

    
        
    def capacity_past_limit(self):
        if self.capacity < len(self.room_guest_list):
            self.clear_guest_list()
            return "5 Person Capacity"
        else: pass

    def favorite_song(self):
        self.load_more_guests()
        self.load_song_selection()       
        for song in self.room_songs_list:           
            if song == self.room_guest_list[0]["favorite song"]:
                return "Whoo!"

                    ## QUESTION: I want to iterate over the list of songs, and check against every index. Could manually add, but seems like a for loop job. 


    def add_drinks_to_guest(self):
        self.load_more_guests()
        self.room_guest_list[0]["drinks"].append(self.bar.bar_drink_list[0]["beer"]["half_pint"])

    def charge_guest_for_drink(self):
        self.load_guest_list()    
        for person in self.room_guest_list:
                person['money'] = person['money'] - self.bar.bar_drink_list[0]["beer"]["half_pint"]

    def guest_drink_list_length(self):
        self.load_guest_list()
        self.add_drinks_to_guest()
        return len(self.room_guest_list[0]["drinks"])

## note for improvement: add drink sold variable

    def add_drink_value_to_admin_cash_in(self):
        self.load_guest_list
        self.admin['total_cash_in'] = self.admin['total_cash_in'] + self.bar.bar_drink_list[0]["beer"]["half_pint"]
        return self.admin['total_cash_in']



        
        



    
    
