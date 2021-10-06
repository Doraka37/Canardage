import random
from random import randrange

def ProtectPlay(Board, value, playerID):
    ## Check a chaque tour de jeu si une case est protégé par le joueur
    Board.BoardGame[value - 1].update({"protected":playerID})
    return Board

def ProtectCheck(Board, value):
    if Board.BoardGame[value - 1]["duck"] == 'empty':
        return False
    return True

def HidePlay(Board, value, value2):
    Board.BoardGame[value2 - 1].update({"hideDuck":Board.BoardGame[value - 1]["duck"]})

    while value < len(Board.BoardGame):
        Board.BoardGame[value - 1].update({"duck":Board.BoardGame[value]["duck"]})
        Board.BoardGame[value - 1].update({"hideDuck":Board.BoardGame[value]["hideDuck"]})
        value += 1
    Board.BoardGame[-1].update({"duck":Board.DuckDrawList[0]})
    Board.DuckDrawList.pop(0)
    return Board

def HideCheck(Board, value, value2, playerID):
    if value2 > value + 1 or value2 < value - 1 or value == value2:
        return False

    if Board.BoardGame[value2 - 1]["duck"] == 'empty':
        return False
    if Board.BoardGame[value2 - 1]["hideDuck"] != 'none':
        return False

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                return True

    return False

def CanarchiePlay(Board, valueList):
    BoardGameTmp = []
    for i in range(6):
        obj = {
            'duck':Board.BoardGame[i]["duck"],
            'hideDuck':Board.BoardGame[i]["hideDuck"]
        }
        BoardGameTmp.append(obj)


    for i in range(6):
        Board.BoardGame[valueList[i] - 1].update({"duck":BoardGameTmp[i]["duck"]})
        Board.BoardGame[valueList[i] - 1].update({"hideDuck":BoardGameTmp[i]["hideDuck"]})

    return Board

def CanarchieCheck(Board):
    return True

def CrazyDancePlay(Board):
    for i in range(6):
        Board.DuckDrawList.append(Board.BoardGame[i]["duck"])
        Board.BoardGame[i].update({"duck":"'none'"})
        if Board.BoardGame[i]["hideDuck"] != 'none':
            Board.DuckDrawList.append(Board.BoardGame[i]["hideDuck"])
            Board.BoardGame[i].update({"hideDuck":"'none'"})

    random.shuffle(Board.DuckDrawList)
    for x in Board.BoardGame:
        x.update({"duck":Board.DuckDrawList[0]})
        Board.DuckDrawList.pop(0)
    return Board

def CrazyDanceCheck(Board):
    return True

def PeaceLovePlay(Board):
    for x in Board.BoardGame:
        x.update({"target":False})

    return Board

def PeaceLoveCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True

    return False

def WalkingDuckPlay(Board, value):
    Board.PlayerList[value - 1]["death"].update({"death":Board.PlayerList[value - 1]["death"] - 1})
    BoardGame.DuckDrawList.append(Board.PlayerList[value - 1]["duck"])

    return Board

def WalkingDuckCheck(Board, value):
    if Board.PlayerList[value - 1]["death"] < 2:
        return False
