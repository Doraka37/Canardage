def Pan(Board, value):
    if PanCheck(Board, value) == True:
        Board = PanPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

def PanPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def PanCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == False:
        return False
    return True

def PanGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True
    return False

def Aim(Board, value):
    if AimCheck(Board, value) == True:
        Board = AimPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

def AimPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":True})
    return Board

def AimCheck(Board, value):
    if Board.BoardGame[value - 1]["target"] == True:
        return False
    return True

def AimGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == False:
            return True
    return False

def Oups(Board, value):
    if OupsCheck(Board, value) == True:
        Board = OupsPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
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
        return False
    elif value == 6 and Board.BoardGame[value - 2]["target"] == False:
        return False
    elif Board.BoardGame[value - 2]["target"] == False and Board.BoardGame[value]["target"] == False:
        return False
    return True

def OupsGlobalCheck(Board):
    for x in Board.BoardGame:
        if x["target"] == True:
            return True
    return False

def DuckyLuck(Board, value):
    if DuckyLuckCheck(Board, value) == True:
        Board = DuckyLuckPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

def DuckyLuckPlay(Board, value):
    Board.BoardGame[value - 1].update({"target":False})
    Board.DeathMove(value)
    return Board

def DuckyLuckCheck(Board, value):
    return True

def DuckyLuckGlobalCheck(Board):
    return True

def AimRight(Board, value):
    if AimRightCheck(Board, value) == True:
        Board = AimRightPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

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

def AimRightGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i < 5 and Board.BoardGame[i + 1]["target"] == False:
            return True
    return False

def AimLeft(Board, value):
    if AimLeftCheck(Board, value) == True:
        Board = AimLeftPlay(Board, value)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

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

def AimLeftGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i > 0 and Board.BoardGame[i - 1]["target"] == False:
            return True
    return False

def TwoForOne(Board, value, value2):
    if TwoForOneCheck(Board, value, value2) == True:
        Board = TwoForOnePlay(Board, value, value2)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
    return Board

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

def TwoForOneGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == False and i < 5 and Board.BoardGame[i + 1]["target"] == False:
            return True
    return False

def DoublePan(Board, value, value2):
    if DoublePanCheck(Board, value, value2) == True:
        Board = DoublePanPlay(Board, value, value2)
        Board.ErrorMessage = 200
    else:
        Board.ErrorMessage = 300
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
        return False

    if Board.BoardGame[value - 1]["target"] == False:
        return False
    if Board.BoardGame[value2 - 1]["target"] == False:
        return False
    return True

def DoublePanGlobalCheck(Board):
    for i in range(Board.BoardGame):
        if Board.BoardGame[i]["target"] == True and i < 5 and Board.BoardGame[i + 1]["target"] == True:
            return True
    return False
