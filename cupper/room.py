class Game:
    def __init__(self):
        self.rooms = []

    def add_room(self):
        new_room = self.rooms.append(Room(len(self.rooms)))
        return new_room

    def is_free_rooms(self):
        for room in self.rooms:
            if not room.is_busy():
                return room

    def get_room_by_id(self, id):
        return self.rooms[id]


class Room:
    def __init__(self, id):
        self.max_channels = 5
        self.user_channels = {}
        self.id = id

    def is_busy(self):
        if len(self.user_channels) == 5:
            return False


GameMain = Game()
GameMain.add_room()
GameMain.add_room()