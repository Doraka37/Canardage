import random
from random import randrange

def Protect(Board, value, playerID):
    Board = ProtectCheck(Board, value)
    if Board.Status == True:
        Board = ProtectPlay(Board, value, playerID)
    return Board

def ProtectPlay(Board, value, playerID):
    ## Check a chaque tour de jeu si une case est protégé par le joueur
    Board.BoardGame[value - 1].update({"protected":playerID})
    return Board

def ProtectCheck(Board, value):
    if Board.BoardGame[value - 1]["protected"] != 'none':
        Board.ErrorMessage = "Cette case est déja protégé"
        Board.Status = False
        return Board

    if Board.BoardGame[value - 1]["duck"] == 'empty':
        Board.ErrorMessage = "Cette case ne possede pas de canard"
        Board.Status = False
        return Board
    Board.ErrorMessage = "La carte a été joué"
    Board.Status = True
    return Board

def ProtectGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["duck"] != "empty" and x['protected'] == 'none':
            return True

    return False

def Hide(Board, value, value2, PlayerID):
    Board = HideCheck(Board, value, value2, PlayerID)
    if Board.Status == True:
        Board = HidePlay(Board, value, value2)
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
        Board.ErrorMessage = "Les cases ne sont pas adjacente"
        Board.Status = False
        return Board

    if Board.BoardGame[value2 - 1]["duck"] == 'empty':
        Board.ErrorMessage = "Cette case ne posede pas de canards"
        Board.Status = False
        return Board
    if Board.BoardGame[value2 - 1]["hideDuck"] != 'none':
        Board.ErrorMessage = "Un canard est déja cacché sous cette case"
        Board.Status = False
        return Board

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                Board.ErrorMessage = "La carte a été joué"
                Board.Status = True
                return Board

    Board.ErrorMessage = "Cette case ne contient pas de canards allié"
    Board.Status = False
    return Board

def HideGlobalCheck(Board, PlayerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == PlayerID:
            playerDuckTmp = player["duck"]

    for i in range(len(Board.BoardGame)):
        if Board.BoardGame[i]["duck"] == playerDuckTmp:
            if i == 0 and Board.BoardGame[i + 1]["hideDuck"] == 'none':
                return True
            elif i == 5 and Board.BoardGame[i - 1]["hideDuck"] == 'none':
                return True
            elif Board.BoardGame[i - 1]["hideDuck"] == 'none' or Board.BoardGame[i + 1]["hideDuck"] == 'none':
                return True

    return False

def Canarchie(Board, valueList):
    valueList = valueList.replace(',', '')
    valueList = valueList.replace('[', '')
    valueList = valueList.replace(']', '')
    Board = CanarchieCheck(Board, valueList)
    if Board.Status == True:
        Board = CanarchiePlay(Board, valueList)
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
        Board.BoardGame[int(valueList[i]) - 1].update({"duck":BoardGameTmp[i]["duck"]})
        Board.BoardGame[int(valueList[i]) - 1].update({"hideDuck":BoardGameTmp[i]["hideDuck"]})

    return Board

def CanarchieCheck(Board, valueList):
    print("len: ", len(valueList))
    for x in valueList:
        print("value: ", x)
    if len(valueList) != 6:
        Board.ErrorMessage = "La liste ne contient pas 6 valeurs"
        Board.Status = False
        return Board

    tmp = ""
    i = 0
    while i < 6:
        tmp = valueList[i]
        j = i + 1
        while j < 6:
            if tmp == valueList[j]:
                Board.ErrorMessage = "Une ou plusieurs valeurs sont en double"
                Board.Status = False
                return Board
            j += 1
        i += 1


    Board.ErrorMessage = "La carte a été joué"
    Board.Status = True
    return Board

def CanarchieGlobalCheck(Board):
    return True

def CrazyDance(Board):
    Board = CrazyDanceCheck(Board)
    if Board.Status == True:
        Board = CrazyDancePlay(Board)
    return Board

def CrazyDancePlay(Board):
    for i in range(6):
        Board.DuckDrawList.append(Board.BoardGame[i]["duck"])
        Board.BoardGame[i].update({"duck":"'none'"})
        if Board.BoardGame[i]["hideDuck"] != 'none':
            Board.DuckDrawList.append(Board.BoardGame[i]["hideDuck"])
            Board.BoardGame[i].update({"hideDuck":"'none'"})

    random.shuffle(Board.DuckDrawList)
    print(Board.DuckDrawList)
    for x in Board.BoardGame:
        print("lol")
        x.update({"duck":Board.DuckDrawList[0]})
        Board.DuckDrawList.pop(0)
    return Board

def CrazyDanceCheck(Board):
    Board.ErrorMessage = "La carte a été joué"
    Board.Status = True
    return Board

def CrazyDanceGlobalCheck(Board):
    return True

def PeaceLove(Board):
    Board = PeaceLoveCheck(Board)
    if Board.Status == True:
        Board = PeaceLovePlay(Board)
    return Board

def PeaceLovePlay(Board):
    for x in Board.BoardGame:
        x.update({"target":False})

    return Board

def PeaceLoveCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            Board.ErrorMessage = "La carte a été joué"
            Board.Status = True
            return Board

    Board.ErrorMessage = "Il n'y a aucune cible sur le plateau"
    Board.Status = False
    return Board

def PeaceLoveGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True

    return False

def WalkingDuck(Board, value):
    Board = WalkingDuckCheck(Board, value)
    if Board.Status == True:
        Board = WalkingDuckPlay(Board, value)
    return Board

def WalkingDuckPlay(Board, value):
    Board.PlayerList[value - 1].update({"death":Board.PlayerList[value - 1]["death"] - 1})
    Board.DuckDrawList.append(Board.PlayerList[value - 1]["duck"])

    return Board

def WalkingDuckCheck(Board, value):
    if Board.PlayerList[value - 1]["death"] == 1:
        Board.ErrorMessage = "Ce joueur n'as aucun canard mort"
        Board.Status = False
        return Board
    if Board.PlayerList[value - 1]["death"] == 6:
        Board.ErrorMessage = "Ce joueur est éliminé"
        Board.Status = False
        return Board
    Board.ErrorMessage = "La carte a été joué"
    Board.Status = True
    return Board

def WalkingDuckGlobalCheck(Board):
    for x in Board.PlayerList:
        if x["death"] > 1 and x["death"] < 6:
            return True
    return False
