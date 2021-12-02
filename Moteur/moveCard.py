import board

def Walk(Board):
    Board = WalkCheck(Board)
    if Board.Status == True:
        Board = WalkPlay(Board)
    return Board

def WalkPlay(Board):
    Board.DuckDrawList.append(Board.BoardGame[0]["duck"])
    Board.DuckDrawList.append(Board.BoardGame[0]["hideDuck"])
    for i in range(len(Board.BoardGame)):
        Board.BoardGame[i - 1].update({"duck":Board.BoardGame[i]["duck"]})
        Board.BoardGame[i - 1].update({"hideDuck":Board.BoardGame[i]["hideDuck"]})
        i += 1
    Board.BoardGame[-1].update({"duck":Board.DuckDrawList[0]})
    Board.BoardGame[-1].update({"hideDuck":'none'})
    Board.DuckDrawList.pop(0)
    return Board

def WalkCheck(Board):
    Board.ErrorMessage = "La carte a été joué"
    Board.Status = True
    return Board

def WalkGlobalCheck(Board):
    return True

def Fulguro(Board, value, PlayerID):
    Board = FulguroCheck(Board, value, PlayerID)
    if Board.Status == True:
        Board = FulguroPlay(Board, value)
    return Board

def FulguroPlay(Board, value):
    tmpDuck = Board.BoardGame[value - 1]["duck"]
    tmpHideDuck = Board.BoardGame[value - 1]["hideDuck"]
    while value > 1:
        Board.BoardGame[value - 1].update({"duck":Board.BoardGame[value - 2]["duck"]})
        Board.BoardGame[value - 1].update({"hideDuck":Board.BoardGame[value - 2]["hideDuck"]})
        value -= 1
    Board.BoardGame[0].update({"duck":tmpDuck})
    Board.BoardGame[0].update({"hideDuck":tmpHideDuck})
    return Board

def FulguroCheck(Board, value, playerID):
    if value < 2 or value > 6:
        Board.ErrorMessage = "La case sélectioné est la premiere case"
        Board.Status = False
        return Board

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value]["duck"]:
                Board.ErrorMessage = "La carte a été joué"
                Board.Status = True
                return Board

    Board.ErrorMessage = "Le canard sélectioné n'est pas un canard allié"
    Board.Status = False
    return Board

def FulguroGlobalCheck(Board, playerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(len(Board.BoardGame)):
        if i > 0 and Board.BoardGame[i]["duck"] == playerDuckTmp:
            return True

    return False

def DuckLeft(Board, value, PlayerID):
    Board = DuckLeftCheck(Board, value, PlayerID)
    if Board.Status == True:
        Board = DuckLeftPlay(Board, value)
    return Board

def DuckLeftPlay(Board, value):
    tmpDuck = Board.BoardGame[value - 1]["duck"]
    tmpHideDuck = Board.BoardGame[value - 1]["hideDuck"]

    Board.BoardGame[value - 1].update({"duck":Board.BoardGame[value - 2]["duck"]})
    Board.BoardGame[value - 1].update({"hideDuck":Board.BoardGame[value - 2]["hideDuck"]})

    Board.BoardGame[value - 2].update({"duck":tmpDuck})
    Board.BoardGame[value - 2].update({"hideDuck":tmpHideDuck})
    return Board

def DuckLeftCheck(Board, value, playerID):
    if value == 1:
        Board.ErrorMessage = "La case sélectioné est la premiere du plateau"
        Board.Status = False
        return Board

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                if Board.BoardGame[value - 2]["duck"] == 'empty':
                    Board.ErrorMessage = "La carte a gauche n'est pas un canard"
                    Board.Status = False
                else:
                    Board.ErrorMessage = "La carte a été joué"
                    Board.Status = True
                return Board

    Board.ErrorMessage = "Le canard sélectioné n'est pas un canard allié"
    Board.Status = False
    return Board

def DuckLeftGlobalCheck(Board, playerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(len(Board.BoardGame)):
        if i > 0 and Board.BoardGame[i]["duck"] == playerDuckTmp:
                if Board.BoardGame[i - 1]["duck"] != 'empty':
                    return True
                else:
                    continue

    return False

def DuckRight(Board, value, PlayerID):
    Board = DuckRightCheck(Board, value, PlayerID)
    if Board.Status == True:
        Board = DuckRightPlay(Board, value)
    return Board

def DuckRightPlay(Board, value):
    tmpDuck = Board.BoardGame[value - 1]["duck"]
    tmpHideDuck = Board.BoardGame[value - 1]["hideDuck"]

    Board.BoardGame[value - 1].update({"duck":Board.BoardGame[value]["duck"]})
    Board.BoardGame[value - 1].update({"hideDuck":Board.BoardGame[value]["hideDuck"]})

    Board.BoardGame[value].update({"duck":tmpDuck})
    Board.BoardGame[value].update({"hideDuck":tmpHideDuck})
    return Board

def DuckRightCheck(Board, value, playerID):
    if value == 6:
        Board.ErrorMessage = "La case sélectioné est la derniere du plateau"
        Board.Status = False
        return Board

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                if Board.BoardGame[value]["duck"] == 'empty':
                    Board.ErrorMessage = "La carte a droite n'est pas un canard"
                    Board.Status = False
                else:
                    Board.ErrorMessage = "La carte a été joué"
                    Board.Status = True
                return Board


    Board.ErrorMessage = "Le canard sélectioné n'est pas un cnard allié"
    Board.Status = False
    return Board

def DuckRightGlobalCheck(Board, playerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(len(Board.BoardGame)):
        if i < 5 and Board.BoardGame[i]["duck"] == playerDuckTmp:
            if Board.BoardGame[i + 1]["duck"] != 'empty':
                return True
            else:
                continue

    return False
