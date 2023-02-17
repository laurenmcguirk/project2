"""
CIS 163 Project 2 - Inheritance - GV Zork - Text-based game
Authors: Allison Scheffer and Lauren McGuirk
Date: February 2023
"""
import random
from datetime import datetime


class Item:
    """
    Item class is a blueprint for storing item information that will
    be used to create a list of items in each room/place of the game.

    Attributes:
        name: str - name of the item, cannot be blank
        description: str - description of the item, cannot be blank
        calories: int - number of calories in food, -500 to 13000 (exclusive)
            0 if not a food item, negative if it will make elf (Prof. Posada) the reject it
        weight: float - weight of the item in pounds, 0 to 500 (exclusive)
    """

    def __init__(self, name: str, description: str, calories: int, weight: float):
        """
        Constructor
        :param name: str - name of the item
            Raises: ValueError is value passed in is blank
        :param description: str - description of the item
            Raises: ValueError if value passed in is blank
        :param calories: int - number of calories in food
            Raises: ValueError if value passed in is not between -500 and 13000
        :param weight: float - weight of the item in pounds
            Raises: ValueError if value passed in is not between 0 and 500
        """
        if name == '':
            raise ValueError('Names entered cannot be blank!')
        self.name = name

        if description == '':
            raise ValueError('Descriptions cannot be blank!')
        self.description = description

        if calories < -500 or calories > 13000:
            raise ValueError('Calories must be between -500 and 13000!')
        self.calories = calories

        if weight < 0 or weight > 500:
            raise ValueError('Weight must be between 0 and 500!')
        self.weight = weight

    def get_name(self) -> str:
        """
        getter for the name attribute
        :return: str - the name of the item
        """
        return self.name

    def get_description(self) -> str:
        """
        getter for the description attribute
        :return: description: str - the description of the item
        """
        return self.description

    def get_calories(self) -> int:
        """
        getter for the calories attribute
        :return: calories: int - number of calories in the item
        """
        return self.calories

    def get_weight(self) -> float:
        """
        getter for the weight attribute
        :return: weight: float - the weight of the item in pounds
        """
        return self.weight

    def set_name(self, new_name: str) -> None:
        """
        setter for the name attribute
        :param new_name: str - the new name for the item
            :raises ValueError: if the str passed in is blank
        """
        if new_name == '':
            raise ValueError('Names entered cannot be blank!')
        self.name = new_name

    def set_description(self, new_des: str) -> None:
        """
        setter for description attribute
        :param new_des: str - the new description for the item
            :raises ValueError if newDes is a blank string
        """
        if new_des == '':
            raise ValueError('Descriptions cannot be blank!')
        self.description = new_des

    def set_calories(self, new_cals: int) -> None:
        """
        setter for the calories attribute
        :param new_cals: int - the new number of calories in the item
            :raises ValueError if number of calories is not between -500 and 13000
        """
        if new_cals < -500 or new_cals > 13000:
            raise ValueError('Calories must be between -500 and 13000!')

    def set_weight(self, new_weight: int) -> None:
        """
        setter for the weight attribute
        :param new_weight: int - the new weight of the Item
            :raises ValueError if the weight is not between 0 and 500
        """
        if new_weight < 0 or new_weight > 500:
            raise ValueError('Weight must be between 0 and 500!')
        self.weight = new_weight

    def __str__(self) -> str:
        """
        method to convert the Item object into a string
        :return: str - representation of the Item
        """
        return f'{self.name} - {self.weight} lb - {self.description}'


class NPC:
    """
    NPC class is a blueprint for storing information about a character
    that can be used in a Location

    Attributes:
        name: str - the name of the character
        description: str - the description of the character
        message_number: int - the index of a message in the messages list
        messages: list - the list of messages that the NPC can say
    """

    def __init__(self, name: str, description: str):
        """
        Constructor
        :param name: str - the name of the character
        :param description: str - the description of the character
        """
        self.name = name
        self.description = description
        self.message_number = 0
        self.messages = []

    def get_name(self) -> str:
        """
        getter for the name attribute
        :return: str - name of the NPC
        """
        return self.name

    def get_description(self) -> str:
        """
        getter for the description attribute
        :return: str - description of the NPC
        """
        return self.description

    def __str__(self) -> str:
        """
        method to convert the NPC object into a string
        return: str - representation of the NPC from its name
        """
        return self.name

    def add_message(self, message: str) -> None:
        """
        method to add messages of the NPC into a list
        :param message: str - message the NPC will say
        """
        self.messages.append(message)

    def get_message(self) -> str:
        """
        adds one to message number to continue down the list until reaching the
        end and resetting to zero
        :return: str - current message indicated by message number
        """
        current_message = self.messages[self.message_number]
        self.message_number += 1
        if self.message_number == len(self.messages):
            self.message_number = 0
        return current_message


class Location:
    """
    Location class is a blueprint for storing information about a location
    that represents a place that can be visited

    Attributes:
        name: str - name of the Location
        description: str - description of the Location
        visited: bool - keeps track if the Location has been visited (True)
            or if it has not been visited (False)
        directions: dict[str, Location] - contains the neighboring locations
            which the player can travel to from this location
        NPCs: List[NPC] - the NPCs that are in the Location
        items: List[Item] - the items that are in the Location
    """

    def __init__(self, name: str, description: str):
        """
        Constructor:
        :param name: str - name of the Location
        :param description: str - description of the Location
        """
        self.name = name
        self.description = description
        self.visited = False
        self.directions = {}
        self.NPCs = []
        self.items = []

    def get_locations(self) -> dict:
        """
        getter for direction attribute
        :return: dict - dictionary of the location's directions
        """
        return self.directions

    def get_name(self) -> str:
        """
        getter for the name attribute
        :return: str - name of the Location
        """
        return self.name

    def get_description(self) -> str:
        """
        getter for the description attribute
        :return: str - description of the Location
        """
        return self.description

    def get_visited(self) -> bool:
        """
        method to check if the location has been visited
        :return: bool - true if yes visited, false if not visited
        """
        if self.visited:
            return True
        else:
            return False

    def set_visited(self) -> None:
        """
        method that changes the visited variable to true
        """
        self.visited = True

    def add_location(self, direction: str, location: 'Location') -> None:
        """
        method to add a location to the neighbors dictionary
        :param: direction: str - direction to the neighbor from this instance of Location
            Raises: ValueError if value entered is blank
            Raises: KeyError if value entered already exists for this instance of Location.
        :param: location: Location - an instance of the Location class that
            can be traveled to from this instance of Location
        """
        if direction == '':
            raise ValueError('Direction entered cannot be blank!')
        if direction in self.directions:
            raise KeyError('This direction already exists!')
        self.directions[direction] = location

    def add_npc(self, npc: NPC) -> None:
        """
        method for adding an NPC to the Location's list of NPCs
        :param: npc: NPC - character to be added to the Location
        """
        self.NPCs.append(npc)

    def get_npcs(self) -> list[NPC]:
        """
        getter for NPCs attribute
        :return: list[NPC] - list of the NPCs in the Location
        """
        return self.NPCs

    def add_item(self, item: Item) -> None:
        """
        method for adding an Item to the Location's item list
        :param: item: Item - item to be added in the location
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        """
        method for removing an Item from the Location's item list
        :param: item: Item - item to be removed from the location
        """
        self.items.remove(item)

    def get_items(self) -> list:
        """
        getter for the items attribute
        :return: list - of items in the Location
        """
        return self.items

    def __str__(self) -> str:
        """
        method for converting the Location object into a string
        :return: str - representation of the Location
        """
        return f'{self.name} - {self.description}'


class Game:
    """
    Game class is a blueprint for storing the logic about each game
    instance.
    The Game is a world of connected locations. The goal is to collect edible items
    and bring them to Posada's classroom in order to be excused from being late
    to class. Each item can have from -500 to 13000 calories. If a player gives
    Posada something inedible, the player will be teleported to a random GV location.
    The player can only carry 30 pounds at a time, so multiple trips to the classroom
    may be needed. Once Posada as been brought enough food with enough calories,
    the player will be excused from their tardiness and the game will end.

    Attributes:
        commands: dict[str] - dictionary of commands for the
          player to call
        items: List[Items] - the items the player currently has
          in their inventory
        current_weight: float - holds current weight player is carrying
            (change to a float?)
        locations: list[Location] - Locations that exist in the world
        current_location: Location - player's current location
        elf_needed_calories: int - number of calories needed to be excused from
            tardiness to class
        game_over: bool - whether the game is still in process or not
    """
    def __init__(self):
        """
        Constructor
        No Parameters
        """
        self.commands = self.setup_commands()
        self.items = []
        self.current_weight = 0
        self.gv_locations = []
        self.island_locations = []
        self.create_world()
        self.current_location = self.first_location()
        self.elf_needed_calories = 2000
        self.game_over = False
        self.count_num_fails = 0

    def first_location(self) -> Location:
        """
        creates a list containing the desired first location, the selects that location.
        :return: Location - the location the player will start in (fudge_shop)
        """
        random_num = random.randint(0, len(self.island_locations) - 1)
        return self.island_locations[random_num]

    def random_gv_location(self) -> Location:
        """
        selects a random location from a list of GV locations
        :return: Location - random location in GV chosen from the list
        """
        random_num = random.randint(0, len(self.gv_locations)-1)
        return self.gv_locations[random_num]

    def create_world(self) -> None:
        """
        This method is where everything in the world is created.
        Each Location is created and then given its directions to its neighboring locations.
        items are added to each location (or the location is not assigned any items).
        NPCs are added to each location (or the location is not assigned any NPCs).
            Each NPC has a list of messages that are added.
        Finally, a list of island locations and a list of GV locations are created
        """
        # locations
        fudge_shop = Location('Fudge Shop', 'A cute little sweets shop and a Mackinac specialty!')
        self.current_location = fudge_shop
        road = Location('Road', 'Just a paved path for cars, and bikes I suppose.')
        museum = Location('Museum', 'Filled with wartime artifacts! '
                                    '\nTake the ferry for a one-way ticket out of here!')
        gv_road = Location('GV Road', 'Welcome to Grand Valley State University!')
        einsteins = Location('Einstein\'s Bagels', 'The best bagel place in town!')
        multi_room = Location('Multipurpose Room', 'Big room full of strange treasures!')
        mackinac = Location('Mackinac Hall', 'The math and computing building--full of nerds of course.')
        mackinac_lower = Location('Mackinac Hall', 'Lower level, a bit spooky down here...')
        mackinac2 = Location('Mackinac Hall', 'Second floor.')
        mackinac2a = Location('Mackinac Hall', 'Second floor, A wing')
        posada_office = Location('Posada\'s office', 'The office of the coolest CS professor!')
        mackinac2b = Location('Mackinac Hall', 'Second floor, B wing')
        posada_room = Location('Posada\'s Classroom', 'Your favorite class!')

        # location directions
        fudge_shop.add_location('Exit', road)

        road.add_location('South', fudge_shop)
        road.add_location('North', museum)

        museum.add_location('South', road)
        museum.add_location('Ferry', gv_road)

        gv_road.add_location('East', einsteins)
        gv_road.add_location('West', mackinac)

        einsteins.add_location('Exit', gv_road)
        einsteins.add_location('Enter', multi_room)

        multi_room.add_location('Exit', einsteins)

        mackinac.add_location('Exit', gv_road)
        mackinac.add_location('Downstairs', mackinac_lower)
        mackinac.add_location('Upstairs', mackinac2)

        mackinac_lower.add_location('Upstairs', mackinac)

        mackinac2.add_location('Downstairs', mackinac)
        mackinac2.add_location('Left', mackinac2a)
        mackinac2.add_location('Right', mackinac2b)

        mackinac2a.add_location('Right', mackinac2)
        mackinac2a.add_location('Left', posada_office)

        posada_office.add_location('Right', mackinac2a)

        mackinac2b.add_location('Left', mackinac2)
        mackinac2b.add_location('Right', posada_room)

        posada_room.add_location('Left', mackinac2b)

        # item needs name, description, calories, and weight
        # Fudge shop items
        choc_fudge = Item('Chocolate fudge', 'Thick and gooey', 900, .5)
        cherry_fudge = Item('Cherry fudge', 'Michigan\'s state fruit in a fudge!', 700, .5)
        pb_fudge = Item('Peanut butter fudge', 'Good thing you\'re not allergic...right?', 850, .5)
        strawberry_fudge = Item('Strawberry fudge', 'Pretty in pink <3', 700, .5)
        fudge_shop.add_item(choc_fudge)
        fudge_shop.add_item(cherry_fudge)
        fudge_shop.add_item(pb_fudge)
        fudge_shop.add_item(strawberry_fudge)

        # road items
        newborn = Item('Newborn baby', 'Cutest orphan ever', 12823, 7)
        horse_poo = Item('Horse poo', 'I wonder why they\'re called \'road apples\'...', -500, 2)
        road.add_item(newborn)
        road.add_item(horse_poo)

        # museum items
        mona = Item('Mona Lisa', 'What\'s she doing here?', 0, 18)
        horse_shoe = Item('Horse Shoe', 'Musty, dusty, and rusty', 0, 7)
        mints = Item('Revolutionary Mints', 'Pretty fresh for a gift shop', 90, .5)
        museum.add_item(mona)
        museum.add_item(horse_shoe)
        museum.add_item(mints)

        # GV Road Items
        dirty_snow = Item('Dirty snow', 'At least it isn\'t yellow...', -100, .2)
        graffiti_rock = Item('Graffiti rock', 'Which frat is advertised today?', 0, 200)
        gv_road.add_item(dirty_snow)
        gv_road.add_item(graffiti_rock)

        # einsteins items
        everything_bagel = Item('Everything bagel', 'All of your hopes and dreams \'sucked into a bagel\'', 400, .3)
        asiago_bagel = Item('Asiago bagel', 'Everything is better with cheese on it', 600, .3)
        choc_muffin = Item('Chocolate muffin', 'Mmmmmm...chocolate', 350, .2)
        vanilla_coffee = Item('Vanilla cream coffee', '\'The best iced coffee\' according to some', 300, .2)
        strawberry_smoothie = Item('Strawberry smoothie', 'Blended, fresh fruit', 95, .3)
        einsteins.add_item(everything_bagel)
        einsteins.add_item(asiago_bagel)
        einsteins.add_item(choc_muffin)
        einsteins.add_item(vanilla_coffee)
        einsteins.add_item(strawberry_smoothie)

        # multipurpose room items
        pancake_plate = Item('Pancake plate', 'Five pancakes smothered in Canadian maple syrup and butter!', 200, 1)
        used_napkin = Item('Used napkin', 'Definitely has a few diseases...', 0, .1)
        chair = Item('Chair', 'A very chair-ey chair', 0, 12)
        multi_room.add_item(pancake_plate)
        multi_room.add_item(used_napkin)
        multi_room.add_item(chair)

        # mackinac 2A items
        loose_notes = Item('Loose notes', 'Whoever wrote these definitely doesn\'t know what was going on', 0, 0.2)
        mackinac2a.add_item(loose_notes)

        # posada office items
        key = Item('Earrings', 'Shiny and Gold', 0, 0.5)
        treat_bag = Item('Bag of treats', 'Cavities, shmavities', 400, 8)
        posada_office.add_item(key)
        posada_office.add_item(treat_bag)

        # mackinac 2B items
        drank_starbucks = Item('Starbucks', 'Half drank and cold, just how I like it', 150, 0.5)
        mackinac2b.add_item(drank_starbucks)

        # NPCs need name and description
        # then add their list of messages
        # fudge shop NPCs
        f_cashier = NPC('Cashier', 'Old lady behind the counter, she\'s almost as sweet as the fudge!')
        f_cashier.add_message('Help yourself to a sample, hun!')
        f_cashier.add_message('I offer a student discount!')
        f_cashier.add_message('Please buy some fudge.')
        f_cashier.add_message('Looking for a job?')
        f_cashier.add_message('Best fudge in Michigan!')
        fudge_shop.add_npc(f_cashier)

        # museum NPCs
        assistant = NPC('Tour Guide', 'Failed history major')
        assistant.add_message('Can I help you?')
        assistant.add_message('Check out these artifacts!')
        assistant.add_message('Good luck on your travels.')
        museum.add_npc(assistant)

        ferry_man = NPC('Ferry Man', 'Captains a magic boat')
        ferry_man.add_message('All aboard!')
        ferry_man.add_message('My life, my love, and my lady is the sea.')
        ferry_man.add_message('One-way ticket to the bermuda triangle of the Great Lakes!')
        museum.add_npc(ferry_man)

        # einsteins NPCs
        e_cashier = NPC('Cashier', 'Friendly college student being the bagel counter')
        e_cashier.add_message('What can I get for you?')
        e_cashier.add_message('Our coffee is pretty good.')
        e_cashier.add_message('Our bagels are the best around!')
        einsteins.add_npc(e_cashier)

        # multipurpose room NPCs
        rando_guy = NPC('Harry Styles', 'Looks like he\'s trying to take a nap.')
        rando_guy.add_message('Shhhhhhhhhhhhh!!!')
        rando_guy.add_message('Leave me alone.')
        rando_guy.add_message('SHHHHHHHHHH!!!!!!!')
        rando_guy.add_message('GO AWAY!')
        multi_room.add_npc(rando_guy)

        # mackinac lower level NPCs
        ghost = NPC('Ghost', 'The phantom of the Mackinac basement!')
        ghost.add_message('I know where Prof. Posada is.')
        ghost.add_message('In your M/W/F classroom.')
        ghost.add_message('Go upstairs twice and right towards to B wing')
        ghost.add_message('BoooooooOOOooOOOOOoo')
        mackinac_lower.add_npc(ghost)

        # mackinac 2A NPCs
        rando_prof = NPC('Professor Dumbledore', 'Wise-looking old man with a pointy hat')
        rando_prof.add_message('Education is important')
        rando_prof.add_message('Get to class.')
        rando_prof.add_message('Why are you still standing here?')
        rando_prof.add_message('Do you believe in magic?')
        rando_prof.add_message('Nevermind, muggle.')
        mackinac2a.add_npc(rando_prof)

        # posada office NPCs
        mini_posada = NPC('Prof. Posada bobble head', 'An odd site, but she\'s friendly')
        mini_posada.add_message('Computer Science is the best!')
        mini_posada.add_message('Take some treats with you!')
        mini_posada.add_message('Hurry along now!')
        posada_office.add_npc(mini_posada)

        # mackinac 2B NPCs
        rando_student = NPC('Stacey', 'Dark-haired girl doing homework on the bench')
        rando_student.add_message('The starbucks isn\'t mine.')
        rando_student.add_message('I saw something weird downstairs...')
        rando_student.add_message('Aren\'t you late?')
        mackinac2b.add_npc(rando_student)

        # posada classroom NPCs
        real_posada = NPC('Professor Posada', 'Your professor, teaching your favorite class')
        real_posada.add_message('You\'re late!')
        real_posada.add_message('I hope you brought snacks for the class!')
        posada_room.add_npc(real_posada)

        # making lists of the island locations
        self.island_locations.append(fudge_shop)

        # making lists of the locations
        self.gv_locations.append(gv_road)
        self.gv_locations.append(einsteins)
        self.gv_locations.append(multi_room)
        self.gv_locations.append(mackinac)
        self.gv_locations.append(mackinac_lower)
        self.gv_locations.append(mackinac2)
        self.gv_locations.append(mackinac2a)
        self.gv_locations.append(posada_office)
        self.gv_locations.append(mackinac2b)

    def show_help(args: None):
        """
        This method tells the player all the actions they can take.
        Ihe method also displays the current time.
        """
        # show help function
        now = datetime.now()
        current_time = now.strftime("%H:%M.%S")
        print('The current time is ' + current_time)
        print('Valid commands are:'
              '\n\'help\' or \'?\': prints available commands'
              '\n\'talk\': talk to NPCs in your current location'
              '\n\'meet\': introduce yourself to an NPC'
              '\n\'go\': type this and your target location to travel (\'go east\')'
              '\n\'items\': show items in inventory'
              '\n\'stats\': show current weight, calories, and calories needed' 
              '\n\'look\': examine surroundings'
              '\n\'take\': pick up item'
              '\n\'give\': give away an item'
              '\n\'ransom\': mystery tool'
              '\n\'quit\': end game')

    def talk(self, name: str):
        """
        This method allows the player to interact with a particular NPC in the Location
        by accessing one of the NPCs messages.
        :param name: str - NPC the player is looking to talk to
        """
        npcs = self.current_location.get_npcs()
        length = len(self.current_location.get_npcs())
        count = 0
        for ppl in npcs:
            if ppl.get_name().lower() == name:
                print(f'You talked to {name}')
                print(f'{name} said: \'{ppl.get_message()}\'')
            else:
                count += 1
        if count == length:
            print(f'There is no one called {name} here.')

    def meet(self, name: str):
        """
        This method allows the player to interact with a particular NPC in the Location
        by accessing the NPCs description.
        :param name: str - NPC the player is looking to learn about
        """
        npcs = self.current_location.get_npcs()
        length = len(self.current_location.get_npcs())
        count = 0
        for ppl in npcs:
            if ppl.get_name().lower() == name:
                print(f'{name}: {ppl.get_description()}')
            else:
                count += 1
        if count == length:
            print(f'There is no one called {name} here.')

    def go(self, direction: str):
        """
        This method allows the player to move to a new location.
        :param direction: str - key related to a location where the player will go
        """
        self.current_location.set_visited()
        if direction == 'enter' or direction == 'exit':
            string = direction + 'ed'
        elif direction == 'ferry':
            string = 'boarded the ' + direction
        else:
            string = 'went ' + direction
        if self.current_weight > 30:
            print('Too much weight! Drop something to continue.')
        else:
            d = direction[0].upper() + direction[1:]
            if d in self.current_location.get_locations().keys():
                self.current_location = self.current_location.get_locations()[d]
                print(f'You {string}')
                if direction == 'ferry':
                    print('          |\\')
                    print('          | \\')
                    print('          |  \\')
                    print('          |___\\')
                    print('          |')
                    print('          |')
                    print('__________|__________')
                    print('\\   o   o   o   o   /')
                    print(' \\                 /')
                    print('  \\               /')
                    print('   \\_____________/')
                    print('The ferry transported you into the bermuda triangle of the Great Lakes! '
                          '\nYou fell into a swirling whirlpool and were magically transported to...'
                          '\nGVSU! Welcome back to your university!')
            else:
                print('That is not a valid direction')

    def show_items(self, args: str = None):
        """
        This method allows the player to view the items that are currently in
        their inventory
        """
        if len(self.items) == 0:
            print('You currently have no items.')
        print('Your current inventory:')
        for i in self.items:
            print(i)

    def look(self, args: str = None):
        """
        This method allows the player to look at what is in their current_location
        such as NPCs, items, and directions to neighboring locations
        """
        print(f'Your current location is {self.current_location}')
        if not self.current_location.get_items():
            print('There are no items')
        else:
            print('This location contains:')
            for item in self.current_location.get_items():
                print(item)

        if not self.current_location.get_npcs():
            print('You are alone')
        else:
            print('You are in the room with: ')
            for person in self.current_location.get_npcs():
                print(person)

        print('You can go:')
        for key in self.current_location.get_locations().keys():
            torf = self.current_location.get_locations().get(key).get_visited()
            if torf:
                print(f'{key} to {self.current_location.get_locations().get(key).get_name()}')
            else:
                print(key)

    def take(self, target: str):
        """
        This method allows the player to pick up items that are in their current_location
        and put them in their inventory
        :param target: str - item the player wants to pick up
        """
        location_items = self.current_location.get_items()
        # items is a pointer to the list of items at current location
        item_found = False
        for item in location_items:
            # item is local variable that computer created in a loop
            # it will point to the items in the collection

            if item.get_name().lower() == target:
                item_found = True
                self.current_location.remove_item(item)
                self.items.append(item)
                self.current_weight += item.get_weight()
                print(f'You took the {target}')
        if not item_found:
            print(f'The item {target} does not exist in your current location')

    def give(self, item_name: str):
        """
        This method allows the player to drop items that are in their inventory and place
        them in their current_location
        :param item_name: str - item the player wants to drop
        """
        item_found = False
        for item in self.items:
            if item.get_name().lower() == item_name:
                self.items.remove(item)
                self.current_location.add_item(item)
                self.current_weight -= item.get_weight()
                print(f'The {item_name} was removed from your inventory and given to '
                      f'{self.current_location.get_name()}')
                item_found = True
                if self.current_location.get_name() == 'Posada\'s Classroom':
                    if len(self.current_location.get_items()) != 0:
                        total_calories = 0
                        for stuff in self.current_location.get_items():
                            if stuff.get_calories() == 0:
                                print('You have given Prof. Posada a non-food item.'
                                      '\nYou have been transported to a random location,'
                                      'you better collect some more food and get back to class!')
                                self.current_location = self.random_gv_location()
                                self.count_num_fails += 1
                                if self.count_num_fails == 3:
                                    print('You gave the professor too many inedible items! Loser!')
                                    self.game_over = True
                            elif stuff.get_calories() < 0:
                                print('You have given Prof. Posada inedible food! She has rejected '
                                      'the food and you have been transported to a random location.'
                                      '\nYou better collect some more food and get back to class!')
                                self.current_location = self.random_gv_location()
                                self.count_num_fails += 1
                                if self.count_num_fails == 3:
                                    print('You gave the professor too many inedible items! Loser!')
                                    self.game_over = True
                            else:
                                total_calories += stuff.get_calories()
                                self.elf_needed_calories -= total_calories
                                if self.elf_needed_calories <= 0:
                                    self.elf_needed_calories = 0
                                    self.game_over = True
        if not item_found:
            print('you can\'t give something you don\'t have')

    # TWO OF OUR OWN COMMANDS
    def weight_and_cals(self):
        """
        This method allows the player to view their current weight and calories
        in their inventory.
        The method also lets the player know if they need to continue collecting
        food items, or if they have enough calories to get excused from their tardiness.
        """
        compiled_cals = 0
        for thing in self.items:
            compiled_cals += thing.get_calories()
        print(f'Your inventory currently weighs {self.current_weight} lbs and contains {compiled_cals} calories.')
        needed = self.elf_needed_calories - compiled_cals
        if needed > 0:
            print(f'You still need to collect {needed} more calories')
        else:
            print('You have enough calories! Now get to class!')

    def ransom(self, item_name: str):
        """
        :param item_name: str - item the player is trying to ransom
        Takes parameter representing the offered item in the users inventory.
        Checks whether item is a newborn baby:
            if so: checks if newborn baby is in current inventory and if NPCs are around to accept ransom (if no NPCs
            prints a message that there is no one to ransom to). Then the NPCs insult the player and exchange the newborn
            for magic fudge that has enough calories to win the game on its own without having any weight. The baby is not
            added to the current location's inventory because there should not be a way to reverse the trade once a
            ransom is made
            if not: tells the player that the item is not worthy of ransom
            if user inventory is empty it tells the user they have nothing to ransom
        """
        if len(self.items) != 0:
            if len(self.current_location.get_npcs()) == 0:
                print('There is no one to accept your ransom')
            for things in self.items:
                if item_name != 'newborn baby':
                    print('You cannot ransom this item')
                elif things.get_name() == 'Newborn baby' and len(self.current_location.get_npcs()) != 0:
                    ppl = self.current_location.get_npcs()
                    print(f'{ppl[0].get_name()} said: WHAT KIND OF MONSTER KIDNAPS AND RANSOMS A BABY?!?!')
                    print(f'As a result of this ruthless transaction, {ppl[0].get_name()} has given you a magic '
                          f'\nand weightless fudge that contains the amount of calories equal to that of the newborn. '
                          f'\nHopefully your are proud enough of this ransom to ignore the guilt swelling inside of '
                          f'\nyou for allowing this baby to be abandoned a second time.')
                    self.items.remove(things)
                    self.current_weight -= things.get_weight()
                    magic = Item('Magic Ransom Fudge',
                                 'Earned the baby\'s calories in a weightless fudge as a result of a ransom', 12823, 0)
                    self.items.append(magic)

        else:
            print('You have no items to ransom.')

    def setup_commands(self) -> dict[str, callable]:
        """
        This method creates a new dictionary. The key consists of commands the player can use.
        The value consists of functions that are called when the player uses each command.
        :return: dict[str, callable] - dictionary of commands and their function that will be executed
        """
        commands = {'help': self.show_help, '?': self.show_help, 'talk': self.talk, 'meet': self.meet,
                    'go': self.go, 'items': self.show_items, 'stats': self.weight_and_cals, 'look': self.look,
                    'take': self.take, 'give': self.give, 'ransom': self.ransom, 'quit': self.quit}
        return commands

    def play(self) -> None:
        """
        This function is the core game loop. It prints a message explaining the game, then shows
        all the available commands.
        While the game is in progress it will loop, prompting the user for a command.
        The function takes the user input and splits it to execute the command.
        When the loop ends, it checks if the elf_needed_calories was less than or equal to 0...
        if it was then a message indicated the player was successful, otherwise
        a failure message appears.
        There is also a 5-minute timer that counts down, once the timer has run out, the game ends
        and the player failed.
        """
        # starts by printing message to describe the game
        print('|\\      /|      /\\      |   /       |\\      /|      /\\     |------\\   |')
        print('| \\    / |     /  \\     |  /        | \\    / |     /  \\    |       |  |')
        print('|  \\  /  |    /____\\    | /         |  \\  /  |    /____\\   |       |  |')
        print('|   \\/   |   /      \\   | \\         |   \\/   |   /      \\  |       |  |')
        print('|        |  /        \\  |  \\        |        |  /        \\ |______/   o')
        print('Welcome to MACKINAC MADNESS! You find yourself in a fudge shop on'
              '\nMackinac Island and you\'re late for your computer science class! You'
              '\nmust collect enough food to feed your classmates (2000 total calories)'
              '\nin order to earn forgiveness from your professor for being late.'
              '\nYou can only carry 20 lbs at once. I\'d try to get a boat out of here'
              '\nASAP if I were you...')
        self.show_help()
        print()

        while not self.game_over:
            user_response = input('What is your command? ').lower()
            tokens = user_response.split()
            command = tokens[0]
            del (tokens[0])
            target = ' '.join(tokens)
            try:
                if target == '':
                    self.commands[command]()
                else:
                    self.commands[command](target)
            except:
                print('That is not a valid command')
            print()
        print('GAME OVER')
        if self.elf_needed_calories <= 0:
            print('You Won!!!')
            print('Despite being late for you\'re computer science class, you appeased your teacher by'
                  '\nbringing her enough food to feed the class. Congratulations!!')
        else:
            print('You have failed!')
            print('You never showed up for class so you were expelled.'
                  '\nBetter luck next time!\n')

    def quit(self, args: str = None):
        """
        This method automatically ends the game
        """
        self.game_over = True


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
