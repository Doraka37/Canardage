import random

class BoardGame:
    DuckList = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    DrawList = []
    BoardGame = [
        {
            'duck':'Empty',
            'Target':False
        },
        {
            'duck':'Empty',
            'Target':False
        },
        {
            'duck':'empty',
            'Target':False
        },
        {
            'duck':'Empty',
            'Target':False
        },
        {
            'duck':'Empty',
            'Target':False
        },
        {
            'duck':'Empty',
            'Target':False
        },
    ]

    def __init__(self, value):
        if value < 2 or value > 6:
            return 404

        for i in range(value):
            for x in range(5):
                self.DrawList.append(self.DuckList[i])

        random.shuffle(self.DrawList)

        for x in self.BoardGame:
            x["duck"] = self.DrawList[0]
            self.DrawList.pop(0)
        print(self.BoardGame)

    def DeathMove(self, value):
        while value < len(self.BoardGame):
            self.BoardGame[value - 1]["duck"] = self.BoardGame[value]["duck"]
            value += 1
        self.BoardGame[value - 1]["duck"] = self.DrawList[0]
        self.DrawList.pop(0)


def DeathMove(value):
    while value < len(BoardGame):
        BoardGame[value - 1]["duck"] = BoardGame[value]["duck"]
        value += 1
    BoardGame[value - 1]["duck"] = DrawList[0]
    DrawList.pop(0)
# Defining main function
def main():
    Board = BoardGame(6)
    Board.DeathMove(2)
    print(Board.BoardGame)


# Using the special variable
# __name__
if __name__=="__main__":
    main()
