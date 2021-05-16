class Guests:
    def __init__(self):
        self.people = [
            {"name": "Wee John", "money": 50, "favorite song": "Castles in the Sky", "drinks": []},
            {"name": "Big Stevie", "money": 300, "favorite song": "Angel of Death", "drinks": []},
            {"name": "Barbra", "money": 500, "favorite song": "The Real Slim Shady", "drinks": []},
        ]

        self.more_people = [
            {"name": "Wee John", "money": 50, "favorite song": "Castles in the Sky", "drinks": []},
            {"name": "Big Stevie", "money": 300, "favorite song": "Angel of Death", "drinks": []},
            {"name": "Barbra", "money": 500, "favorite song": "The Real Slim Shady", "drinks": []},
            {"name": "Janet", "money": 0, "favorite song": "Tequila", "drinks": []},
            {"name": "Karen", "money": 150, "favorite song": "No Women No Cry", "drinks": []},
            {"name": "Scott", "money": 60, "favorite song": "Dancing in the Moonlight", "drinks": []},
            {"name": "Jack", "money": 15, "favorite song": "This is America", "drinks": []},
            {"name": "Conrad", "money": 75, "favorite song": "Original Nuttah", "drinks": []}
        ]
        
        self.guests_guest_list = []

    def add_guest_to_guests_guest_list(self):
        for person in self.people:
            self.guests_guest_list.append(person)     
        return self.guests_guest_list


    def guest_list_length(self):
        return len(self.guests_guest_list)

    def add_more_people_to_guest_list(self):
        for person in self.more_people:
            self.guests_guest_list.append(person)
        return self.guests_guest_list

