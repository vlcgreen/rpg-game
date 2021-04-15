# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.Health = health
        self.Power = power

    def attack(self, opponent):
        opponent.Health -= self.Power
        print("{} does {} damage to {}.".format(self.name, self.Power, opponent.name))

        
    def alive(self):
        if self.Health > 0:
            return True
    
    def print_status(self):
        print("{} have {} health and {} power.".format(self.name, self.Health, self.Power))

class Hero(Character):
    def __init__(self, name, health = 10, power = 5):
        self.name = name
        super(Hero, self).__init__(health, power)

class Goblin(Character):
    def __init__(self, name, health = 6, power = 2):
        self.name = name
        super(Goblin, self).__init__(health, power)
    # def print_status(self):
    #     print("The goblin has {} health and {} power.".format(self.Health, self.Power))

class Zombie(Character):
    def __init__(self, name, health = 6, power = 2):
        self.name = name
        super(Zombie, self).__init__(health, power)
    def alive(self):
        return True
    # def print_status(self):
    #     print("The zombie has {} health and {} power.".format(self.Health, self.Power))


def main():
    hero = Hero('Jack')
    goblin = Goblin('Gollum')
    zombie = Zombie('Harold')



    while zombie.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
            # if goblin.Health <= 0:
            #     print("The goblin is dead.")

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Goblin attacks hero
            zombie.attack(hero)
            if hero.Health <= 0:
                print("You are dead.")


main()
