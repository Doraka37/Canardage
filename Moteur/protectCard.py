import random
from random import randrange

def Protect(Board, value, playerID):
    Board = ProtectCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = ProtecBoard(Board, value, playerID)
    return Board

def ProtectPlay(Board, value, playerID):
    ## Check a chaque tour de jeu si une case est protégé par le joueur
    Board.BoardGame[value - 1].update({"protected":playerID})
    return Board

def ProtectCheck(Board, value):
    if Board.BoardGame[value - 1]["protected"] != 'none':
        Board.ErrorMessage = 901
        return Board

    if Board.BoardGame[value - 1]["duck"] == 'empty':
        Board.ErrorMessage = 902
        return Board
    Board.ErrorMessage = 200
    return Board

def ProtectGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["duck"] != "empty" and x['protected'] == 'none':
            return True

    return False

def Hide(Board, value, value2, PlayerID):
    Board = HideCheck(Board, value, value2, PlayerID)
    if Board.ErrorMessage == 200:
        Board = HidePlBoardard, value, value2)
    return Board

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
        Board.ErrorMessage = 1001
        return Board

    if Board.BoardGame[value2 - 1]["duck"] == 'empty':
        Board.ErrorMessage = 1002
        return Board
    if Board.BoardGame[value2 - 1]["hideDuck"] != 'none':
        Board.ErrorMessage = 1003
        return Board

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                Board.ErrorMessage = 200
                return Board

    Board.ErrorMessage = 1004
    return Board

def HideGlobalCheck(Board, PlayerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["duck"] == playerDuckTmp:
            if i == 0 and Board.BoardGame[i + 1]["hideDuck"] == 'none':
                return True
            elif i == 5 and Board.BoardGame[i - 1]["hideDuck"] == 'none':
                return True
            elif Board.BoardGame[i - 1]["hideDuck"] == 'none' or Board.BoardGame[i + 1]["hideDuck"] == 'none':
                return True

    return False

def Canarchie(Board, valueList):
    Board = CanarchieCheck(Board, valueList)
    if Board.ErrorMessage == 200:
        Board = CanarcBoarday(Board, valueList)
    return Board

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

def CanarchieCheck(Board, valueList):
    if len(valueList) != 6:
        Board.ErrorMessage = 1102
        return Board

    tmp = ""
    i = 0
    while i < 6:
        tmp = valueList[i]
        j = i + 1
        while j < 6:
            if tmp == valueList[j]:
                Board.ErrorMessage = 1101
                return Board
            j += 1
        i += 1


    Board.ErrorMessage = 200
    return Board

def CanarchieGlobalCheck(Board):
    return True

def CrazyDance(Board):
    Board = CrazyDanceCheck(Board)
    if Board.ErrorMessage == 200:
        Board = CrazyDBoardlay(Board)
    return Board

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
    Board.ErrorMessage = 200
    return Board

def CrazyDanceGlobalCheck(Board):
    return True

def PeaceLove(Board):
    Board = PeaceLoveCheck(Board)
    if Board.ErrorMessage == 200:
        Board = PeaceLBoarday(Board)
    return Board

def PeaceLovePlay(Board):
    for x in Board.BoardGame:
        x.update({"target":False})

    return Board

def PeaceLoveCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            Board.ErrorMessage = 200
            return Board

    Board.ErrorMessage = 1301
    return Board

def PeaceLoveGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True

    return False

def WalkingDuck(Board, value):
    Board = WalkingDuckCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = WalkingDuckPlay(Board, value)
    return Board

def WalkingDuckPlay(Board, value):
    Board.PlayerList[value - 1]["death"].update({"death":Board.PlayerList[value - 1]["death"] - 1})
    BoardGame.DuckDrawList.append(Board.PlayerList[value - 1]["duck"])

    return Board

def WalkingDuckCheck(Board, value):
    if Board.PlayerList[value - 1]["death"] < 2:
        Board.ErrorMessage = 200
        return Board
    Board.ErrorMessage = 1401
    return Board

def WalkingDuckGlobalCheck(Board):
    for x in Board.PlayerList:
        if x["death"] > 1:
            return True

    return False
