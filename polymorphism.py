# Parent Class
class dungeon:
    lvlRequirement = '50'
    classRequirement = 'knight'

    def checkRequirements(self):
        playerLvl = input('What is your level? \n')
        playerClass = input('What is your class? \n').lower()
        if (self.lvlRequirement <= playerLvl and self.classRequirement == playerClass):
            print('You are allowed to enter the dungeon!')
        else:
            print('You do not meet the requirements \nto enter this dungeon...')

# Child Class
class realm(dungeon):
    manaRequirement = '200'
    maxPlayers = 100

    def checkRequirements(self):
        playerLvl = input('What is your level? \n')
        playerClass = input('What is your class? \n').lower()
        playerMana = input('What is your mana count? \n')
        if (self.lvlRequirement <= playerLvl and self.classRequirement == playerClass and self.manaRequirement <= playerMana):
            print('You are allowed to enter the realm!')
        else:
            print('You do not meet the requirements \nto enter this realm...')

# Child Class
class subspace(dungeon):
    staminaRequirement = '350'
    maxPlayers = 125

    def checkRequirements(self):
        playerLvl = input('What is your level? \n')
        playerClass = input('What is your class? \n').lower()
        playerStamina = input('What is your stamina count? \n')
        if (self.lvlRequirement <= playerLvl and self.classRequirement == playerClass and self.staminaRequirement <= playerStamina):
            print('You are allowed to enter the subspace!')
        else:
            print('You do not meet the requirements \nto enter this subspace...')

enterDungeon = dungeon()
enterDungeon.checkRequirements()

enterRealm = realm()
enterRealm.checkRequirements()

enterSubspace = subspace()
enterSubspace.checkRequirements()
