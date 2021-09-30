# This is the parent class
class military:
    branchName = ''
    headquarters = ''
    numOfEmployees = 873264
    leaderName = ''
    budget = 1000000

# These are child classes
class airForce(military):
    numOfAircrafts = 376
    numOfHelicopters = 452
    numOfPilots = 289

class navy(military):
    numOfShips = 296
    numOfSubmarines = 328
