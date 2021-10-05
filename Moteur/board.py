import random
from random import randrange
import moveCard
import protectCard
import attackCard

class ClassBoardGame:
    DuckList = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    DuckDrawList = []
    PlayerList = [
        {
            'duck':'red',
            'death':0,
            'id':0
        },
        {
            'duck':'blue',
            'death':0,
            'id':0
        },
        {
            'duck':'green',
            'death':0,
            'id':0
        },
        {
            'duck':'yellow',
            'death':0,
            'id':0
        },
        {
            'duck':'orange',
            'death':0,
            'id':0
        },
        {
            'duck':'purple',
            'death':0,
            'id':0
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

    def __init__(self, value):
        if value < 2 or value > 6:
            return 404

        for i in range(value):
            self.PlayerList[i].update({"death":1})
            self.PlayerList[i].update({"id":randrange(1000000000)})
            for x in range(5):
                self.DuckDrawList.append(self.DuckList[i])

        for i in range(5):
            self.DuckDrawList.append("empty")
        random.shuffle(self.DuckDrawList)

        for x in self.BoardGame:
            x.update({"duck":self.DuckDrawList[0]})
            self.DuckDrawList.pop(0)

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

Board = ClassBoardGame(4)

def test():
    global Board
    print(Board.BoardGame)
    Board = moveCard.WalkPlay(Board)

def main():
    valueList = [4, 3, 5, 2, 6, 1]
    global Board
    print(Board.BoardGame, "\n")
    Board = attackCard.PanPlay(Board, 2)
    print(Board.BoardGame)


# Using the special variable
# __name__
if __name__=="__main__":
    main()
