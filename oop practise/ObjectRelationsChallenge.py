#challenge on object relations

class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print("Model: ",self.model)
        print("Color: ",self.color)
    
class SedanEngine:
    def start(self):
        print("Car has started")
    
    def stop(self):
        print("Car has stopped")


class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine
    
    def setStart(self):
        self.engine.start()
    
    def setStop(self):
        self.engine.stop()


#challenge2
class Player:
    def __init__(self, ID, name, teamNmae):
        self.ID = ID
        self.name = name
        self.teamName = teamNmae
    

class Team:
    def __init__(self,name):
        self.name = name
        self.players = []

    def addPlayer(self,otherPlayer):
        self.players.append(otherPlayer)
        return self.players
    
    def getNumberOfPlayers(self):
        return len(self.players)


class School:
    def __init__(self,name):
        self.name = name
        self.teams = []
    
    def addTeam(self,otherTeam):
        self.teams.append(otherTeam)
        return self.teams

    def getTotalPlayersInSchool(self):
        count = 0
        for i in self.teams:
            count += (i.getNumberOfPlayers())

        return count

p1 = Player("Harris", 1, "Red");
p2 = Player("Carol", 2, "Red");

p3 = Player("Johnny", 1, "Blue");
p4 = Player("Sarah", 2, "Blue");

red_team=Team("Red Team")
red_team.players.append(p1)
red_team.players.append(p2)

blue_team=Team("Blue Team")
blue_team.players.append(p2)
blue_team.players.append(p3)

mySchool=School("My School")
mySchool.teams.append(red_team)
mySchool.teams.append(blue_team)

print("Total players in my school:", mySchool.getTotalPlayersInSchool())
