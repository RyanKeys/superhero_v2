import random


class Ability:
    def __init__(self, name, max_damage=0):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_kill(self,num_kills):
        self.kills += num_kills

    def add_death(self,num_deaths):
        self.deaths += num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
        if self.abilities == []:
            return 0

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt=0):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            hero_attack = self.attack()
            opponent.take_damage(hero_attack)

            opponent_attack = opponent.attack()
            self.take_damage(opponent_attack)

            if self.is_alive() == False:
                print(f"{self.name} died!")
                opponent.add_kill(1)
                self.add_death(1)
            if opponent.is_alive() == False:
                print(f"{opponent.name} is dead!")
                self.add_kill(1)
                opponent.add_death(1)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


class Weapon(Ability):
    def attack(self):
        half_dmg = self.max_damage/2
        return random.randint(half_dmg, self.max_damage)


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero == True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)
