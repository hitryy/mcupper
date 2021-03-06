from game.game import Game
from game.room import Room


class GameManager:
    """
    Главный класс, отвечающий за игры в каждой комнате:
        - отборочные комнаты
        - финальные комнаты
    """

    def __init__(self):
        """
        Инициализация объекта
        """

        self.allowed_users_id_for_final = {}

        self.qualifying_game = Game(Room.DEFAULT_NAME, self)
        self.final_game = Game(Room.FINAL_NAME, self)

    def get_qualifying_game(self):
        """
        Возврат игры отборочного этапа
        """

        return self.qualifying_game

    def get_final_game(self):
        """
        Возврат игры финального этапа
        :return: объект финальной игры
        """

        return self.final_game

    def add_user_id_to_final_room(self, room_id, user_id):
        """
        Добавить игрока, который выиграл в отборочном этапе в список допущенных к игре
        в финальном этапе
        :param room_id: номер финальной комнаты
        :param user_id: id допущенного пользователя
        """

        if user_id in self.allowed_users_id_for_final:
            self.allowed_users_id_for_final[room_id].append(user_id)
        else:
            self.allowed_users_id_for_final[room_id] = [user_id]

    def delete_disconnected_users_from_all_rooms_in_all_games(self, channel):
        """
        Удалить отключенного пользователя из всех комнат
        :param channel: канал пользователя (websocket)
        """

        self.qualifying_game.delete_disconnected_user_from_rooms(channel)
        self.final_game.delete_disconnected_user_from_rooms(channel)

    def get_room_based_on_type_and_id(self, room_type, id):
        """
        Вернуть комнату, полагаясь на тип комнаты и её уникальный номер
        :param room_type: тип комнаты - отборочный, финальный
        :param id: номер комнаты
        :return: объект комнаты
        """

        if room_type == Room.FINAL_NAME:
            return self.final_game.get_room_by_id(id)

        return self.qualifying_game.get_room_by_id(id)


# Создание глобального объекта - игровой менеджер
GameManager = GameManager()
