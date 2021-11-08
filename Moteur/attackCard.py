def Pan(Board, value):
    Board = PanCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = PanPlay(Board, value)
    return Board

def PanPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def PanCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == False:
        Board.ErrorMessage = 101
        return Board
    Board.ErrorMessage = 200
    return Board

def PanGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True
    return False

def Aim(Board, value):
    Board = AimCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = AimPlay(Board, value)
    return Board

def AimPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":True})
    return Board

def AimCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == True:
        Board.ErrorMessage = 201
        return Board
    Board.ErrorMessage = 200
    return Board

def AimGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == False:
            return True
    return False

def Oups(Board, value):
    Board = OupsCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = OupsPlay(Board, value)
    return Board

def OupsPlay(Board, value):
    if value == 1:
        Board.BoardGame[value].update({"target":False})
    elif value == 6:
        Board.BoardGame[value - 2].update({"target":False})
    elif Board.BoardGame[value - 2]["target"] == True:
        Board.BoardGame[value - 2].update({"target":False})
    else:
        Board.BoardGame[value].update({"target":False})
    Board.DeathMove(value)
    return Board

def OupsCheck(Board, value):
    if value == 1 and Board.BoardGame[value]["target"] == False:
        Board.ErrorMessage = 301
        return Board
    elif value == 6 and Board.BoardGame[value - 2]["target"] == False:
        Board.ErrorMessage = 301
        return Board
    elif Board.BoardGame[value - 2]["target"] == False and Board.BoardGame[value]["target"] == False:
        Board.ErrorMessage = 301
        return Board
    Board.ErrorMessage = 200
    return Board

def OupsGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True
    return False

def DuckyLuck(Board, value):
    Board = DuckyLuckCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = DuckyLuckPlay(Board, value)
    return Board

def DuckyLuckPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def DuckyLuckCheck(Board, value):
    Board.ErrorMessage = 200
    return Board

def DuckyLuckGlobalCheck(Board):
    return True

def AimRight(Board, value):
    Board = AimRightCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = AimRightPlay(Board, value)
    return Board

def AimRightPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.BoardGame[value].update({"target":True})
    return Board

def AimRightCheck(Board, value):
    if value > 5:
        Board.ErrorMessage = 501
        return Board
    if Board.BoardGame[value]["target"] == True:
        Board.ErrorMessage = 502
        return Board
    Board.ErrorMessage = 200
    return Board

def AimRightGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i < 5 and Board.BoardGame[i + 1]["target"] == False:
            return True
    return False

def AimLeft(Board, value):
    Board = AimLeftCheck(Board, value)
    if Board.ErrorMessage == 200:
        Board = AimLeftPlay(Board, value)
    return Board

def AimLeftPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.BoardGame[value - 2].update({"target":True})
    return Board

def AimLeftCheck(Board, value):
    if value < 2:
        Board.ErrorMessage = 601
        return Board
    if Board.BoardGame[value - 2]["target"] == True:
        Board.ErrorMessage = 602
        return Board
    Board.ErrorMessage = 200
    return Board

def AimLeftGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i > 0 and Board.BoardGame[i - 1]["target"] == False:
            return True
    return False

def TwoForOne(Board, value, value2):
    Board = TwoForOneCheck(Board, value, value2)
    if Board.ErrorMessage == 200:
        Board = TwoForOnePlay(Board, value, value2)
    return Board

def TwoForOnePlay(Board, value, value2):
    Board.BoardGame[value - 1].update({"target":True})
    Board.BoardGame[value2 - 1].update({"target":True})
    return Board

def TwoForOneCheck(Board, value, value2):
    if value2 > value + 1 or value2 < value - 1 or value == value2:
        Board.ErrorMessage = 701
        return Board

    if Board.BoardGame[value - 1]["target"] == True:
        Board.ErrorMessage = 702
        return Board
    if Board.BoardGame[value2 - 1]["target"] == True:
        Board.ErrorMessage = 702
        return Board
    Board.ErrorMessage = 200
    return Board

def TwoForOneGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == False and i < 5 and Board.BoardGame[i + 1]["target"] == False:
            return True
    return False

def DoublePan(Board, value, value2):
    Board = DoublePanCheck(Board, value, value2)
    if Board.ErrorMessage == 200:
        Board = DoublePanPlay(Board, value, value2)
    return Board

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
        Board.ErrorMessage = 801
        return Board

    if Board.BoardGame[value - 1]["target"] == False:
        Board.ErrorMessage = 802
        return Board
    if Board.BoardGame[value2 - 1]["target"] == False:
        Board.ErrorMessage = 802
        return Board
    Board.ErrorMessage = 200
    return Board

def DoublePanGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i < 5 and Board.BoardGame[i + 1]["target"] == True:
            return True
    return False
