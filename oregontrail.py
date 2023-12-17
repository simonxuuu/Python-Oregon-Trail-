import random
import sys
import os
Running = True
attempts = 1
def clear():
    os.system('clear')
    
def intro():
    name = input('What is your name?')
    print(f'Be prepared for the best journey of your lifetime, {name}')
    print(f'Remember, {name}. You must be good to people.')
    print(f'What bad you do will come back to you, {name}.')
    print("You embark on the journey of the Oregon Trail with a group.")
    input('Press ENTER to continue')
    clear()
    print("Your best friend thinks you have been stealing food.")
    input('What is your response?\n')
    clear()
    print('The group is unsatisfied with your response.')
    input('What is your explanation?\n')
    clear()
    print('It appears that your explanation was sufficient for reconciliation.')
    input('Do you sleep? You have 100 miles left to go tomorrow with your group.\n')
    clear()
    print('You see your group approaching you.')
    input('Press ENTER to continue.')
    print('They ask you to leave.')
    input('What is your response?\n')
    clear()
    print('Your response made them angry. They took all of your belongings and left you stranded along on the Oregon Trail.')
    input('Press ENTER to continue')
    print('You must fend for yourself now.')
    clear()
    
#intro()

class Pet:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.health = 100
        self.hunger = 0
        self.happiness = 100
    def pet(self):
        print(f'You pet "{self.name}", making him happier.')
        self.happiness += 50
    def update(self):
        if self.hunger > 50:
            self.health -= self.hunger / 10
        if self.health <= 0:
            print(f'{name} died.')
            del self
        self.hunger += 10
        print(f'{self.name}, your pet\nhp: {self.health}\nhunger: {self.hunger}\nhappiness: {self.happiness}')
        

class ItemClass:
    def __init__(self, name, can_damage, safety, edible, food_size):
        self.name = name
        self.can_damage = can_damage
        self.safety = safety
        self.edible = edible
        self.food_size = food_size

class InventoryClass:
    def __init__(self):
        self.capacity = 20
        self.items = []
        self.names = []

    def update_name(self):
        self.names = [item.name for item in self.items]

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f'You added a {item.name} to your inventory.')
        else:
            print('You have no more space.')

    def remove_item(self, index):
        del self.items[index]

    def drop_item(self):
        self.view_items()
        try:
            index = int('Select index of item you want to remove.\n')
            del self.items[index]
        except:
            print('Invalid response.')

    def view_items(self):
        self.update_name()
        display(self.names)

item_values = {
    "raw meat": ['raw meat', False, False, True, 50],
    "cooked meat": ['cooked meat', False, True, True, 75],
    "bow": ['bow', True, False, False, 0],
    "wooden projectile launcher that has a mysterious combustion system": [
        'wooden projectile launcher that has a mysterious combustion system', True, False, False, 0]

}

item_types = [key for key in item_values.keys()]

animal_list = ['cat','dog','deer','elk','cow','horse','rat','bird','wolf','fox','bear','mountain lion','shark','falcon']

def chance(number):
    if random.random() < number:
        return True

def severity_calc(number, adjective):
    if 10 < number <= 25:
        print(f'You are slightly {adjective}.')
    elif 25 < number <= 50:
        print(f'You are moderately {adjective}.')
    elif 50 < number <= 100:
        print(f'You are extremely {adjective}.')
    elif number > 100:
        print(f'You are LIFE-THREATENINGLY {adjective.upper()}.')
        
def display(items):
    if len(items) == 0:
        print('There are no items to use.')
        return None
    for i, item in enumerate(items):
        print(f'{i}. {item}')

class PlayerClass:
    def __init__(self):
        self.inventory = inventory
        self.alive = True
        self.health = float(100)
        self.disease = float(0)
        self.hunger = float(0)
        self.thirst = float(0)
        self.distance = 100
        self.sleep_deprivation = float(0)
        self.days = 0
        self.hoursLeft = 5
        self.pets = []
        self.options = {
            "travel": self.travel,
            "cook": self.cook,
            "eat": self.eat,
            "hunt": self.hunt,
            "find water": self.find_water,
            "view inventory": self.inventory.view_items,
            "drop item": self.inventory.remove_item,
            "search": self.search,
            "sleep": self.sleep
        }
        self.optionList = [key for key in self.options.keys()]
        self.events = {
            "wolf_attack": self.wolf_attack,
            "trader": self.trader,
            "ride": self.a_man_offers_you_a_ride,
            "house": self.abandoned_house,
            "dog": self.dog,
            "find pet" : self.pet_finder,
            "flood": self.flood,
            "aliens": self.aliens
        }
        self.eventList = [key for key in self.events.keys()]
        
    

    def next_day(self):
        self.hoursLeft = random.randrange(4, 6)
        print('You wake up to a sunny day.')
        severity_calc(self.disease, "sick")
        self.days += 1
        self.random_event()
        
    def flood(self):
        print('You lose everything to a flash flood.')
        self.inventory.items.clear()

    def random_event(self):
        if chance(0.75):
            self.events[random.choice(self.eventList)]()
            
    def view_pets(self):
        if not self.pets:
            print("You don't have pets anymore.")
        for i, pet in enumerate(self.pets):
                print(f'{i}. {pet.name}, {pet.type}')
        user_choice = input('Do you want to feed your pets?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            self.inventory.update_name()
            display(self.inventory.names)
            user_choice = None
            if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
            if not user_choice:
                print('Canceled.')
                return None
            elif self.inventory.items[int(user_choice)].can_damage is True:
                print('For some reason, you chose to do that to your pets?')
                for pet in self.pets:
                    print(f'{pet.name} died.')
                    self.inventory.add_item(ItemClass(*item_values['raw meat']))
                    self.inventory.capacity -= 20
                    print('You lost 20 space.')
                self.pets.clear()
                return None
            elif self.inventory.items[int(user_choice)].edible is True:
                print('You feed all your pets.')
                for pet in self.pets:
                    pet.hunger = 0
        else:
            print('You probably should feed them.')
        user_choice = input('Do you want to pet your pets?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            for pet in self.pets:
                pet.pet()
        else:
            print('That is not very nice of you.')
            
    def pet_finder(self):
        type = random.choice(animal_list)
        print(f'You stumble upon a {type}. It seems friendly. What do you use?')
        self.inventory.update_name()
        display(self.inventory.names)
        user_choice = None
        if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
        #if user_choice > len(self.inventory.names):
        #    return None
        if not user_choice:
            print(f'The {type} walks away.')
            return None
        elif self.inventory.items[int(user_choice)].can_damage is True:
            print(f'You successfully defended yourself against a {type}!')
            self.inventory.add_item(ItemClass(*item_values['raw meat']))
        elif self.inventory.items[int(user_choice)].edible is True:
            print(f"You feed the {type}. It appears to love you now. What do you name it?")
            name = input()
            if not name:
                name = 'Pet'
            self.pets.append(Pet(type, name))
            print('List of pets:')
            for i, pet in enumerate(self.pets):
                print(f'{i}. {pet.name}, {pet.type}')
            self.inventory.capacity += 20
            print('You gained 20 inventory space!')
            if "view pets" not in self.options:
                self.options["view pets"] = self.view_pets
    def aliens(self):
        print('You stumble upon a large metallic disk.')
        user_choice = input('It appears to have an entrance. Do you enter?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            print('You enter the metallic disk.')
            input("Press ENTER to continue.")
            print('The inside feels much larger than the outside.')
            input("Press ENTER to continue.")
            print('Every single surface feels perfectly sterile.')
            input("Press ENTER to continue.")
            print('You suddenly feel an overwhelming tiredness.')
            input("Press ENTER to continue.")
            print('You wake up to grey humanoids inspecting your brain.')
            input("Press ENTER to continue.")
            user_choice = input('Do you resist?\nCHOICES: YES, NO')
            if user_choice.lower() == 'yes':
                print('You get teleported down to an unfamiliar place.')
                self.distance += 50
            else:
                print('You allow the aliens to perform an operation on you.')
                input('Press ENTER to continue.')
                self.health = 100
                self.thirst = 0
                self.hunger = 0
                self.disease = 50
                print('You feel rujuvenated with an overwhelming sense of dread.')
        else:
            print('Better safe than sorry!')
            return None
    def dog(self):
        print('You spot a dog within the depths of brush.')
        user_choice = input('Do you want to follow the dog?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            print('The dog sprints through the forest, you follow its trail of dust.')
            input('Press ENTER to continue.')
            print('The dog leads you to the edge of a cliff.')
            input('Press ENTER to continue.')
            print('The dog signals that its owner requires help because of a fall.')
            user_choice = input('Do you help the man?\nCHOICES: YES, NO')
            if user_choice.lower() == 'yes':
                print('You slowly climb down the cliff and see a man lying down.')
                user_choice = input('Do you bring the man to the dog?\nCHOICES: YES, NO')
                if user_choice.lower() == 'yes':
                    print('You carry the man up the cliff and let him down in front of his dog.')
                    input('Press ENTER to continue.')
                    print('The man thanks you profusely and offers you some aid for helping him.')
                    user_choice = input('Do you accept?\nCHOICES: YES, NO')
                    if user_choice.lower() == 'yes':
                        print('You follow him to his cabin.')
                        input('Press ENTER to continue.')
                        print('He offers you a glass of water and a feast.')
                        user_choice = input('Do you accept?\nCHOICES: YES, NO')
                        if user_choice.lower() == 'yes':
                            print('You are now satiated. You bring along with you the leftovers.')
                            for i in range(10):
                                self.inventory.add_item(ItemClass(*item_values['cooked meat']))
                            input('Press ENTER to continue.')
                            print('You bid farewell to the man, thanking him for his gracious contributions.')
                        else:
                            print('You politely decline and you go your own way.')
                            input('Press ENTER to continue.')
                            print('Maybe you should have accepted.')
                            input('Press ENTER to continue.')
                    else:
                        print('You politely decline and you go your own way.')
                        input('Press ENTER to continue.')
                        print('Maybe you should have accepted.')
                        input('Press ENTER to continue.')
                else:
                    print('You politely decline and you go your own way.')
                    input('Press ENTER to continue.')
                    print('Maybe you should have accepted. Be a better person.')
                    input('Press ENTER to continue.')
            else:
                print('You politely decline and you go your own way.')
                input('Press ENTER to continue.')
                print('Maybe you should have accepted.')
                input('Press ENTER to continue.')
        else:
            print('You tell the dog, "No."')
            input('Press ENTER to continue.')
            print('Maybe you should have followed the dog.')
            input('Press ENTER to continue.')
            print('You walk towards the dogs direction after it leaves.')
            input('Press ENTER to continue.')
            print('You fall off a cliff.')
            input('Press ENTER to continue.')
            print('Maybe the dog was warning you?')
            input('Press ENTER to continue.')
            self.health -= 75

    def wolf_attack(self):
        print('You see a wolf from a distance.\nWhat do you use on the wolf?')
        self.inventory.update_name()
        display(self.inventory.names)
        user_choice = None
        if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
        if not user_choice:
            print('The wolf slaps you in the face and steals everything from you.')
            self.inventory.items.clear()
            return None
        elif self.inventory.items[int(user_choice)].can_damage is True:
            print('You successfully defended yourself against a wolf!')
            self.inventory.add_item(ItemClass(*item_values['raw meat']))
        else:
            print('Did you really think that would work? \n'
                  'The wolf slaps you in the face and steals everything from you.')
            self.inventory.items.clear()

    def trader(self):
        print('A masked man wearing a fur coat walks up to you.')
        user_choice = input('Do you run away?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            return None
        else:
            pass
        print('He asks, "What brings you here?"')
        print('This interaction feels oddly familiar to you. You respond, "New opportunity."')
        input('Press ENTER to continue')
        print('He replies, "I have an opportunity for you. Give me all that you have, and a gift to you, I will grant.')
        user_choice = input('Do you give the man everything?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            self.inventory.items.clear()
            for i in range(1):
                self.inventory.add_item(ItemClass(*item_values['cooked meat']))
            print('In exchange for everything you have, the man gives you 1 cooked meat.')
            input('Press ENTER to continue')
            print('You look down at all the meat he has given you and wonder, "What type of meat is this?"')
            input('Press ENTER to continue')
            print('You return to thank the man, but there is no one to be seen.')
            input('Press ENTER to continue')
            print('Hopefully, there will be no unwanted visitors.')
            input('Press ENTER to continue')
        elif user_choice.lower() == 'no':
            self.health -= 25
            print('Ow! The man slaps you. Was that worth it?')
            input('Press ENTER to continue')
            print('You check your belongings. You have nothing.')
            input('Press ENTER to continue')
            self.inventory.items.clear()

    def a_man_offers_you_a_ride(self):
        print('You hear the faint sound of a horse galloping towards your direction with a wagon.\n'
              'You turn around and see a well-kempt suited man on the horse.\n'
              '''He approaches you and asks, "You're not from around here, aren't you, partner?"''')
        print('''You reply, "No sir, heading west.''')
        input('Press ENTER to continue')
        print('He responds, "That is mighty fine, partner. Want to hitch a ride in my wagon?')
        user_choice = input('Do you want to ride with the man?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            print('You hop inside the wagon, seeing dozens of skulls.')
            input('Press ENTER to continue')
            print('The man notices that you noticed the skulls.')
            input('Press ENTER to continue')
            print('He tells you that "It is not safe out here."')
            input('Press ENTER to continue')
            print('You close your eyes and hope you will not add to the collection.')
            input('Press ENTER to continue')
            print('You wake up with a skull facing you.')
            input('Press ENTER to continue')
            print('He asks, "Ah you finally woke up? I got to turn around, good luck on your journey, traveler.')
            input('Press ENTER to continue')
            print('He bids farewell to you and rides off into the distance.')
            input('Press ENTER to continue')
            self.distance -= 30
            if self.distance <= 0:
                print(
                    f'You arrive in Oregon after {self.days} days on the trail. You can finally rest now. You have demonstrated your excellence and determination.')
                sys.exit()
            else:
                print(f'You traveled 30 miles, with {self.distance} miles remaining.')
        else:
            print('He says, "All right, good luck partner."')
            input('Press ENTER to continue')
            print('Best not to test your luck, right?')
            input('Press ENTER to continue')
            print('You trip on a rock. Maybe you should be more trusting to people.')
            self.health -= 5

    def abandoned_house(self):
        print('You stumble upon an abandoned house.')
        user_choice = input('Do you want to enter the house?\nCHOICES: YES, NO')
        if user_choice.lower() == 'yes':
            print('You open the door. You hear shuffling inside one of the rooms.')
            user_choice = input('Do you want to continue?\nCHOICES: YES, NO')
            if user_choice.lower() == 'yes':
                print('You continue searching the house.')
                input('Press ENTER to continue.')
                print('You see the shadow of a man.')
                input('Press ENTER to continue')
                print('He looks at you.')
                input('Press ENTER to continue')
                print('You slowly walk out the door.')
                input('Press ENTER to continue')
                print('You bolt out the door and start sprinting.')
                input('Press ENTER to continue')
                print('You feel exhausted.')
                input('Do you want to continue running?\n') # No choice given
                print('You collapse.')
                input('Press ENTER to continue')
                print('You hear footsteps behind you.')
                input('Do you want to run?\n')
                print('You see the same figure you saw in the house hovering above you.')
                print('The figure says to you, "Do you need help?"')
                user_choice = input('Do you accept?\nCHOICES: YES, NO')
                if user_choice.lower() == 'yes':
                    for i in range(20):
                        self.inventory.add_item(ItemClass(*item_values['bow']))
                    self.health = 100
                    self.thirst = 0
                    self.hunger = 0
                    self.disease = 0
                    print('You suddenly feel rejuvenated!')
                else:
                    print('The figure is unsatisfied with your response.')
                    print('You feel an overwhelming sense of dread. What is going to happen?')
                    self.health = 0
        else:
            print('You walk away. Who knows what could have been in there?')
            return None


    def sleep(self):
        print('You go to sleep.')
        self.next_day()
        self.disease = 0
        self.sleep_deprivation -= random.randrange(20,65) - ((self.hunger + self.thirst) / 3)
        if self.sleep_deprivation < 0: self.sleep_deprivation = 0

    def travel(self):
        if self.sleep_deprivation >= 50:
            print('You are too lethargic to travel.')
            return None
        travel_distance = (random.randrange(1, 5) * self.hoursLeft)
        self.distance -= travel_distance
        self.hunger += travel_distance * 2
        self.thirst += travel_distance * 2
        if self.distance <= 0:
            print(
                f'You arrive in Oregon after {self.days} days on the trail. You can finally rest now. You have demonstrated your excellence and determination.')
            print(f'You won with {attempts} attempts.')
            sys.exit()
        else:
            print(f'You traveled {travel_distance} miles, with {self.distance} miles remaining.')
        self.next_day()

    def cook(self):
        print('You light a fire, what do you cook?')
        self.inventory.update_name()
        display(self.inventory.names)
        user_choice = None
        if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
        if not user_choice:
            print('Canceled.')
            return None
        else:
            user_choice = int(user_choice)
            if self.inventory.items[user_choice].edible is True:
                self.inventory.remove_item(user_choice)
                self.inventory.add_item(ItemClass(*item_values['cooked meat']))
                print('You successfully cooked meat.')
            else:
                print(f'You throw "{self.inventory.names[user_choice]}" into the fire.')
                self.inventory.remove_item(user_choice)

    def eat(self):
        print('You open your inventory. What do you eat?')
        self.inventory.update_name()
        display(self.inventory.names)
        user_choice = None
        if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
        if not user_choice:
            print('Canceled.')
            return None
        else:
            user_choice = int(user_choice)
            if self.inventory.items[user_choice].edible:
                self.hunger = 0
                self.health += 25
                if self.health >= 100:
                    self.health = 100
                if self.inventory.items[user_choice].safety is False:
                    self.disease += 25
                print(f'You ate {self.inventory.names[user_choice]}.')
                self.inventory.remove_item(user_choice)
            else:
                print(f'You eat {self.inventory.names[user_choice]}. You should not have eaten that.')
                self.inventory.remove_item(user_choice)
                self.health = 0

    def hunt(self):
        if chance(0.9):  # Chance to find deer
            print('You see a deer from a distance.\nWhat do you use on the deer?')
            self.inventory.update_name()
            display(self.inventory.names)
            user_choice = None
            if len(self.inventory.names) != 0: user_choice = (input('Select a number.\n'))
            if not user_choice:
                print('Canceled.')
                return None
            elif self.inventory.items[int(user_choice)].can_damage is True:
                print('You successfully hunted a deer!')
                self.inventory.add_item(ItemClass(*item_values['raw meat']))
            else:
                print('The deer ran away.')

            self.hunger += 25
            self.thirst += 25  # Physical exertion makes people thirsty & hungry

    def find_water(self):
        if chance(0.75):  # Chance to find water
            print('You find a stream nearby. Do you drink the water?')
            user_choice = input('OPTIONS: YES, NO')
            if user_choice.lower() == 'yes':
                if chance(0.5):
                    print('You drank water with no ill effects.')
                    self.thirst = 0
                else:
                    print('You drink water. You now have dysentery.')
                    self.thirst = 0
                    self.disease += 25  # Gives sickness if water unsafe
        else:
            print('You failed in your search for water.')

    def search(self):
        find = random.choice(item_types)
        if chance(0.75):
            self.inventory.add_item(ItemClass(*item_values[find]))
        else:
            print("Your search was unsuccessful.")

    def prompt(self):
        for i, activity in enumerate(self.options):
            print(f'{i}. {activity}')
        user_choice = input(f'What would you like to do?\n')
        if not user_choice:
            print('Canceled')
            return None
        else:
            try:
                self.optionList = [key for key in self.options.keys()]
                number = int(user_choice)
                user_choice = self.optionList[number]
            except:
                pass
            if user_choice in self.options:
                self.options[user_choice]()
        self.hoursLeft -= 1
        print('A few hours go by.')
        if self.hoursLeft <= 2:
            print('It is getting dark.')
        self.hunger += 5
        self.thirst += 5

    def update(self):
        if chance(0.1) and self.pets:
            find = random.choice(item_types)
            self.inventory.add_item(ItemClass(*item_values[find]))
            print('Your pet brought you something!')
        if self.health <= 0:
            self.alive = False
            return None
        if self.hoursLeft == 0:
            self.next_day()
        severity_calc(self.hunger, "hungry")
        severity_calc(self.thirst, "dehydrated")
        severity_calc(self.sleep_deprivation,"tired")
        if self.sleep_deprivation > 75:
            self.health -= self.hunger / 10
        if self.hunger > 50:
            self.health -= self.hunger / 10
        if self.thirst > 50:
            self.health -= self.thirst / 10
        self.health -= self.disease / 10
        if self.health <= 0:
            self.alive = False
            return None
        print(f'hp: {self.health}\nthirst: {self.thirst} \nhunger: {self.hunger} \nsickness: {self.disease}')
        if self.pets:
            for pet in self.pets:
                pet.update()

    def run(self):
        while self.alive:
            clear()
            self.update()
            self.prompt()
            if self.health <= 0:
                print(f'You perished after spending {player.days} days on the Oregon Trail.')
                break


while Running:
    inventory = InventoryClass()  # Initializes the objects
    player = PlayerClass()
    player.run()
    answer = input('Do you want to play again?\nCHOICES: YES, NO')
    if answer.lower() == 'yes':
        pass
        attempts += 1
    else:
        sys.exit()
