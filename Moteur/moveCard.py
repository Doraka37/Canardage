import board

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
