import board

def Walk(Board):
    if WalkCheck(Board) == True:
        Board = WalkPlay(Board)
    else:
        Board.ErrorMessage = "Card can't by play"
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
    return True

def WalkGlobalCheck(Board):
    return True

def Fulguro(Board, value, PlayerID):
    if FulguroCheck(Board, value, PlayerID) == True:
        Board = FulguroPlay(Board, value)
    else:
        Board.ErrorMessage = "Card can't by play"
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
        return False

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value]["duck"]:
                return True

    return False

def FulguroGlobalCheck(Board, playerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(Board.BoardGame):
        if i > 0 and Board.BoardGame[i]["duck"] == playerDuckTmp:
            return True

    return False

def DuckLeft(Board, value, PlayerID):
    if DuckLeftCheck(Board, value, PlayerID) == True:
        Board = DuckLeftPlay(Board, value)
    else:
        Board.ErrorMessage = "Card can't by play"
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
        return False

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                return True

    return False

def DuckLeftGlobalCheck(Board, playerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(Board.BoardGame):
        if i > 0 and Board.BoardGame[i]["duck"] == playerDuckTmp:
            return True

    return False

def DuckRight(Board, value, PlayerID):
    if DuckRightCheck(Board, value, PlayerID) == True:
        Board = DuckRightPlay(Board, value)
    else:
        Board.ErrorMessage = "Card can't by play"
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
        return False

    for player in Board.PlayerList:
        if player["id"] == playerID:
            if player["duck"] == Board.BoardGame[value - 1]["duck"]:
                return True

    return False

def DuckRightGlobalCheck(Board, PlayerID):
    playerDuckTmp = ""
    for player in Board.PlayerList:
        if player["id"] == playerID:
            playerDuckTmp = player["duck"]

    for i in range(Board.BoardGame):
        if i < 5 and Board.BoardGame[i]["duck"] == playerDuckTmp:
            return True

    return False
