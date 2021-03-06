import random
from random import randrange
import moveCard
import protectCard
import attackCard

class ClassBoardGame:
    ErrorMessage = ""
    Status = True
    endGame = False
    DuckList = ['rouge', 'bleue', 'vert', 'jaune', 'orange', 'violet']
    DuckDrawList = []
    CardList = [
        {
            'id':1,
            'number':13
        },
        {
            'id':2,
            'number':11
        },
        {
            'id':3,
            'number':1
        },
        {
            'id':4,
            'number':1
        },
        {
            'id':5,
            'number':2
        },
        {
            'id':6,
            'number':2
        },
        {
            'id':7,
            'number':1
        },
        {
            'id':8,
            'number':1
        },
        {
            'id':9,
            'number':3
        },
        {
            'id':10,
            'number':2
        },
        {
            'id':11,
            'number':1
        },
        {
            'id':12,
            'number':1
        },
        {
            'id':13,
            'number':1
        },
        {
            'id':14,
            'number':1
        },
        {
            'id':15,
            'number':6
        },
        {
            'id':16,
            'number':1
        },
        {
            'id':17,
            'number':3
        },
        {
            'id':18,
            'number':3
        },
    ]
    CardDrawList = []
    CardDiscardList = []
    PlayerList = [
        {
            'duck':'rouge',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
        {
            'duck':'bleue',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
        {
            'duck':'vert',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
        {
            'duck':'jaune',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
        {
            'duck':'orange',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
        {
            'duck':'violet',
            'death':0,
            'id':0,
            'card': [],
            'name' : ""
        },
    ]
    BoardGame = [
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
        {
            'duck':'none',
            'hideDuck':'none',
            'target':False,
            'protected':'none'
        },
    ]

    def __init__(self, value, idList):
        if value < 2 or value > 6:
            self.ErrorMessage = "Le nombre de joueur doit etre comprit entre 2 et 6"
            self.Status = False

        else:
            for i in range(value):
                self.PlayerList[i].update({"death":1})
                self.PlayerList[i].update({"id":idList[i]["id"]})
                for x in range(5):
                    self.DuckDrawList.append(self.DuckList[i])

            for i in range(5):
                self.DuckDrawList.append("empty")
            random.shuffle(self.DuckDrawList)

            for x in self.BoardGame:
                x.update({"duck":self.DuckDrawList[0]})
                self.DuckDrawList.pop(0)

            for x in self.CardList:
                for i in range(x["number"]):
                    self.CardDrawList.append(x["id"])
            random.shuffle(self.CardDrawList)

    def DeathMove(self, value):
        if self.BoardGame[value - 1]["duck"] == 'empty':
            return
        for player in self.PlayerList:
            if player["duck"] == self.BoardGame[value - 1]["duck"]:
                player["death"] += 1

        if self.BoardGame[value - 1]["hideDuck"] != 'none':
            self.BoardGame[value - 1].update({"duck":self.BoardGame[value - 1]["hideDuck"]})
            self.BoardGame[value - 1].update({"hideDuck":'none'})
        else:
            while value < len(self.BoardGame):
                self.BoardGame[value - 1].update({"duck":self.BoardGame[value]["duck"]})
                self.BoardGame[value - 1].update({"hideDuck":self.BoardGame[value]["hideDuck"]})
                value += 1
            self.BoardGame[-1].update({"duck":self.DuckDrawList[0]})
            self.BoardGame[-1].update({"hideDuck":'none'})
            self.DuckDrawList.pop(0)
        if checkEnd(self.PlayerList) == True:
            self.endGame = True

def checkEnd(playerList):
    i = 0
    for x in playerList:
        if x["death"] > 0 and x["death"] < 6:
            i += 1
    if i > 1:
        return False
    return True

def test():
    return

def PlayCard(Board, ID, value, value2, valueList, playerID):
    Board.ErrorMessage = "Une erreur est survenue"
    Board.Status = False
    ID = int(ID)
    value = int(value)
    value2 = int(value2)
    playerID = int(playerID)
    switcher = {
        1: lambda : attackCard.Pan(Board, value),
        2: lambda : attackCard.Aim(Board, value),
        3: lambda : attackCard.Oups(Board, value),
        4: lambda : attackCard.DuckyLuck(Board, value),
        5: lambda : attackCard.AimRight(Board, value),
        6: lambda : attackCard.AimLeft(Board, value),
        7: lambda : attackCard.TwoForOne(Board, value, value2),
        8: lambda : attackCard.DoublePan(Board, value, value2),
        9: lambda : protectCard.Protect(Board, value, playerID),
        10: lambda : protectCard.Hide(Board, value, value2, playerID),
        11: lambda : protectCard.Canarchie(Board, valueList),
        12: lambda : protectCard.CrazyDance(Board),
        13: lambda : protectCard.WalkingDuck(Board, value),
        14: lambda : protectCard.PeaceLove(Board),
        15: lambda : moveCard.Walk(Board),
        16: lambda : moveCard.Fulguro(Board, value, playerID),
        17: lambda : moveCard.DuckLeft(Board, value, playerID),
        18: lambda : moveCard.DuckRight(Board, value, playerID),
    }

    return switcher.get(ID, lambda : Board)()


def GlobalCheckCard(Board, ID, playerID):
    Board.ErrorMessage = "Une erreur est survenue"
    Board.Status = False
    ID = int(ID)
    playerID = int(playerID)
    switcher = {
        1: lambda : attackCard.PanGlobalCheck(Board),
        2: lambda : attackCard.AimGlobalCheck(Board),
        3: lambda : attackCard.OupsGlobalCheck(Board),
        4: lambda : attackCard.DuckyLuckGlobalCheck(Board),
        5: lambda : attackCard.AimRightGlobalCheck(Board),
        6: lambda : attackCard.AimLeftGlobalCheck(Board),
        7: lambda : attackCard.TwoForOneGlobalCheck(Board),
        8: lambda : attackCard.DoublePanGlobalCheck(Board),
        9: lambda : protectCard.ProtectGlobalCheck(Board),
        10: lambda : protectCard.HideGlobalCheck(Board, playerID),
        11: lambda : protectCard.CanarchieGlobalCheck(Board),
        12: lambda : protectCard.CrazyDanceGlobalCheck(Board),
        13: lambda : protectCard.WalkingDuckGlobalCheck(Board),
        14: lambda : protectCard.PeaceLoveGlobalCheck(Board),
        15: lambda : moveCard.WalkGlobalCheck(Board),
        16: lambda : moveCard.FulguroGlobalCheck(Board, playerID),
        17: lambda : moveCard.DuckLeftGlobalCheck(Board, playerID),
        18: lambda : moveCard.DuckRightGlobalCheck(Board, playerID),
    }

    return switcher.get(ID, lambda : Board)()

def getBoard(value, idList):
    Board = ClassBoardGame(value, idList)
    return Board

if __name__ == '__main__':
    idList = [
        {
            "id":213231,
            "isHere":True
        },
        {
            "id":345234,
            "isHere":False
        },
        {
            "id":213213213,
            "isHere":True
        },
        {
            "id":324123123,
            "isHere":False
        },
        {
            "id":213213123,
            "isHere":False
        },
        {
            "id":2132144123123,
            "isHere":False
        },
    ]
    list = [1,2,3,3,5]
    i = 6
    Board = getBoard(i, idList)
    print(Board.BoardGame)
    print(protectCard.ProtectGlobalCheck(Board))
