def PanPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def PanCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == False:
        return False
    return True

def AimPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":True})
    return Board

def AimCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == True:
        return False
    return True

def OupsPlay(Board, value):
    if value > 1 and Board.BoardGame[value - 2]["target"] == True:
        Board.BoardGame[value - 2].update({"target":False})
    else:
        Board.BoardGame[value].update({"target":False})
    Board.DeathMove(value)
    return Board

def OupsCheck(Board, value):
    if value > 1 and Board.BoardGame[value - 2]["target"] == True:
        return True
    elif value < 6 and Board.BoardGame[value]["target"] == True:
        return True
    return False

def DuckyLuckPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def DuckyLuckCheck(Board, value):
    return True

def AimRightPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.BoardGame[value].update({"target":True})
    return Board

def AimRightCheck(Board, value):
    if value > 5:
        return False
    if Board.BoardGame[value]["target"] == True:
        return False
    return True

def AimLeftPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.BoardGame[value - 2].update({"target":True})
    return Board

def AimLeftCheck(Board, value):
    if value < 2:
        return False
    if Board.BoardGame[value - 2]["target"] == True:
        return False
    return True

def TwoForOnePlay(Board, value, value2):
    Board.BoardGame[value - 1].update({"target":True})
    Board.BoardGame[value2 - 1].update({"target":True})
    return Board

def TwoForOneCheck(Board, value, value2):
    if value2 > value + 1 or value2 < value - 1 or value == value2:
        return False

    if Board.BoardGame[value - 1]["target"] == True:
        return False
    if Board.BoardGame[value2 - 1]["target"] == True:
        return False
    return True

def DoublePanPlay(Board, value, value2):
    Board.BoardGame[value - 1].update({"target":False})
    Board.BoardGame[value2 - 1].update({"target":False})
    if value2 > value:
        Board.DeathMove(value2)
        Board.DeathMove(value)
    else:
        Board.DeathMove(value)
        Board.DeathMove(value2)
    return Board

def DoublePanCheck(Board, value, value2):
    if value2 > value + 1 or value2 < value - 1 or value == value2:
        return False

    if Board.BoardGame[value - 1]["target"] == False:
        return False
    if Board.BoardGame[value2 - 1]["target"] == False:
        return False
    return True
