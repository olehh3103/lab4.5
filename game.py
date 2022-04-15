"""my lab"""

import doctest

class Room:
    """
    class works with rooms
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room.")
    >>> kitchen.description
    'A dank and dirty room.'
    """
    def __init__(self, room_name: str) -> None:
        """
        init function
        """
        self.room_name = room_name
        self.description = None
        self.link = {}
        self.character = None
        self.item = None

    def set_description(self, description: str):
        """
        function set description
        """
        self.description = description

    def link_room(self, room_obj: object, room_loc: str):
        """
        function puts room_obj and room_loc into the dict
        """
        self.link[room_loc] = room_obj

    def set_character(self, character: object):
        """
        function set character
        """
        self.character = character

    def set_item(self, item: object):
        """
        function set item
        """
        self.item = item

    def get_character(self):
        """
        function returns character
        """
        return self.character

    def get_details(self):
        """
        function returns details
        """
        print(self.room_name)
        print("--------------------")
        print(self.description)
        for i in self.link:
            print(f"The {self.link[i].room_name} is {i}")

    def get_item(self):
        """
        Function returns item
        """
        return self.item

    def move(self, command: str):
        """
        function makes a move
        """
        return self.link[command]


class Enemy():
    """
    class wors with enemys
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_weakness("cheese")
    >>> dave.weakness
    'cheese'
    """
    counter = 0
    def __init__(self, name_of_enemy: str, character: str) -> None:
        """
        init function
        """
        self.name_of_enemy = name_of_enemy
        self.character = character
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation: str):
        """
        function sets conversation
        """
        self.conversation = conversation

    def set_weakness(self, weakness: str):
        """
        function sets weakness
        """
        self.weakness = weakness

    def describe(self):
        """
        function describes who is in a room
        """
        print(f"{self.name_of_enemy} is here!")
        print(self.character)

    def talk(self):
        """
        function print what the enemy says
        """
        print(f"[{self.name_of_enemy} says]: {self.conversation}")

    def fight(self, fight_with):
        """
        function checks if the player can win the enemy
        """
        if fight_with == self.weakness:
            Enemy.counter += 1
            print(f"You fend {self.name_of_enemy} off with the {self.weakness}")
            return True
        print(f"{self.name_of_enemy} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        """
        function return a num of wins
        """
        return Enemy.counter

class Item:
    """
    class works with items
    >>> cheese = Item("cheese")
    >>> cheese.set_description("A large and smelly cheese")
    >>> cheese.description
    'A large and smelly cheese'
    """
    def __init__(self, item_name) -> None:
        """
        init function
        """
        self.item_name = item_name
        self.description = None

    def set_description(self, description: str):
        """
        function sets description
        """
        self.description = description

    def describe(self):
        """
        function describes an item
        """
        print(f"The [{self.item_name}] is here - {self.description}")

    def get_name(self):
        """
        function returns name of item
        """
        return self.item_name

if __name__ == "__main__":
    print(doctest.testmod())
