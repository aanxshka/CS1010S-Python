######### DO NOT REMOVE THIS LINE ##########
from hungry_games import *
############################################      


#############
##  Task 1 ##
#############

class Tribute(Person):


    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        self.hunger = 0 
        # add hunger property




    ############
    #  Task 1b #
    ############
    def get_hunger(self):
        return self.hunger
    # definition of get_hunger here




    ############
    #  Task 1c #
    ############
    def add_hunger(self,hunger):
        self.hunger += hunger
        if self.hunger >= 100:
            return super().go_to_heaven()
    # definition of add_hunger here




    ############
    #  Task 1d #
    ############
    def reduce_hunger(self,hunger):
        self.hunger -= hunger
        if self.hunger <= 0:
            self.hunger = 0 
    # definition of reduce_hunger here




    #############
    ##  Task 2 ##
    #############
    def eat(self,food):
        if isinstance(food,Food) and food in self.get_inventory():
            self.hunger -= food.get_food_value()
            if isinstance(food,Medicine):
                self.health += food.get_medicine_value()
            if self.get_hunger() <= 0:
                self.hunger = 0
            if self.get_health() >= 100:
                self.health = 100
            self.remove_item(food)




    ############
    #  Task 3a #
    ############
    def get_weapons(self):
        tpl = ()
        for i in self.get_inventory():
            if isinstance(i,Weapon):
                tpl += (i,)
        return tpl
                




    ############
    #  Task 3b #
    ############
    def get_food(self):
        tpl = ()
        for i in self.get_inventory():
            if isinstance(i,Food):
                tpl += (i,)
        return tpl




    ############
    #  Task 3c #
    ############
    def get_medicine(self):
        tpl = ()
        for i in self.get_inventory():
            if isinstance(i,Medicine):
                tpl += (i,)
        return tpl




    #############
    ##  Task 4 ##
    #############
    def attack(self,living_thing, weapon):
        if weapon in self.get_inventory():
            harm = weapon.damage()
            living_thing.health -= harm


    from hungry_games_classes import *
from engine import *
import random
# Rename XX_AI to YourName_AI
class Anushka_AI(Tribute):
    def choose_weapon(self):
        for i in self.get_weapons():
            if isinstance(i, Weapon) and not isinstance(i,RangedWeapon):
                return i 
                break
            
    def next_action(self):
        #Task 1 pick up weapon and add to inventory
        wp = self.choose_weapon()
        objs = self.objects_around()
        for i in objs:
            if isinstance(i,Thing):
                return ("TAKE", i)
        
        #Task 1 kill animal
        for i in objs:
            if isinstance(i,Animal):
                return ("ATTACK", i, wp)
      
        #Task 1 take food after killing animal
        for i in objs:
            if isinstance(i,Food):
                return ("TAKE", i)
        #Task 2 kill harmless tributes
        for i in objs:
            if isinstance(i,Tribute):
                return ("ATTACK", i, wp)
                
            
        #Task 2 move around and explore
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        
                                                                                                    
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2                                                            
your_AI = Anushka_AI # Modify if you changed the name of the AI class
from hungry_games_classes import *
from engine import *
import random
# Rename XX_AI to YourName_AI
class Anushka_AI(Tribute):
    def choose_weapon(self):
        for i in self.get_weapons():
            if isinstance(i, Weapon) and not isinstance(i,RangedWeapon):
                return i 
                break
            
    def next_action(self):
        #Task 1 pick up weapon and add to inventory
        wp = self.choose_weapon()
        objs = self.objects_around()
        for i in objs:
            if isinstance(i,Thing):
                return ("TAKE", i)
        
        #Task 1 kill animal
        for i in objs:
            if isinstance(i,Animal):
                return ("ATTACK", i, wp)
      
        #Task 1 take food after killing animal
        for i in objs:
            if isinstance(i,Food):
                return ("TAKE", i)
        #Task 2 kill harmless tributes
        for i in objs:
            if isinstance(i,Tribute):
                return ("ATTACK", i, wp)
                
            
        #Task 2 move around and explore
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        
                                                                                                    
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2                                                            
your_AI = Anushka_AI # Modify if you changed the name of the AI class







