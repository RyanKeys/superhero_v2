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
        random_value = random.randint(0, int(self.max_damage))
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

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

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

    def stats(self):
        for hero in self.heroes:
            kd = f"{hero.kills} / {hero.deaths}"
            print(f"{hero.name} K/D Ratio: {kd}")

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        return

    def team_health(self):
        total = 0
        for hero in self.heroes:
            total += hero.current_health
        return total

    def attack(self, other_team):

        fighter = random.choice(self.heroes)
        opponent = random.choice(other_team.heroes)

        while fighter.current_health > 0 and opponent.current_health > 0:

            fighter.fight(opponent)


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name?")
        max_damage = input("What is the max damage of the ability?")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the name of your weapon?")
        max_damage = input(f"What is the max damage of {name}?")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the name of your armor?")
        max_block = input(f"What is the max block of {name}?")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.abilities.append(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.abilities.append(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.armors.append(armor)
        return hero

    def build_team_one(self):
        team_name = input("What's your team's name?")
        hero_amt = int(input("How many heroes are on your team?"))
        self.team_one = Team(team_name)
        for hero in range(hero_amt):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
        return self.team_one

    def build_team_two(self):
        team_name = input("What's your team's name?")
        hero_amt = int(input("How many heroes are on your team?"))
        self.team_two = Team(team_name)
        for hero in range(hero_amt):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        if self.team_one.team_health() < 1:
            print(self.team_two.name + " wins!")
            
        elif self.team_two.team_health() < 1:
            print(self.team_one.name + " wins!")
            

        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
