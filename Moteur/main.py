from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from random import randrange
from flask_cors import CORS
from random import randrange
import pandas as pd
from multiprocessing import Process
import ast
import sched, time
import board
import json

Board = ""
app = Flask(__name__)
CORS(app)
api = Api(app)
afkWile = True
started = False

idList = [
    {
        "id":213231,
        "isHere":True
    },
    {
        "id":345234,
        "isHere":False
    },
    {
        "id":213213213,
        "isHere":True
    },
    {
        "id":324123123,
        "isHere":False
    },
    {
        "id":0,
        "isHere":False
    },
    {
        "id":0,
        "isHere":False
    },
]

playerList = [
    {
        "id":0,
        "name":"",
        "color":"red"
    },
    {
        "id":0,
        "name":"",
        "color":"blue"
    },
    {
        "id":0,
        "name":"",
        "color":"green"
    },
    {
        "id":0,
        "name":"",
        "color":"yellow"
    },
    {
        "id":0,
        "name":"",
        "color":"orange"
    },
    {
        "id":0,
        "name":"",
        "color":"purple"
    },
]

class playCard(Resource):
    def post(self):
        global Board
        global started
        started = True
        if started == False:
            response = app.response_class(
                response=json.dumps({"data":"game is not started"}),
                status=300,
                mimetype='application/json'
            )
        else:
            value1 = request.form.get("value1")
            value2 = request.form.get("value2")
            valueList = request.form.get("valueList")
            playerID = request.form.get("playerID")
            cardID = request.form.get("cardID")
            print("acrd id: ", cardID)
            Board = board.PlayCard(Board, cardID, value1, value2, valueList, playerID)
            print(Board.ErrorMessage)
            if Board.ErrorMessage == 200:
                print("pd1")
                if Board.CardDrawList == []:
                    Board.CardDrawList = Board.CardDiscardList
                    random.shuffle(Board.CardDrawList)
                    CardDiscardList = []
                Board.CardDiscardList.append(cardID)
                cardDraw = Board.CardDrawList[0]
                Board.CardDrawList.pop(0)
                response = app.response_class(
                    response=json.dumps({"data":cardDraw}),
                    status=Board.ErrorMessage,
                    mimetype='application/json'
                )
            else:
                print("pd2")
                response = app.response_class(
                    response=json.dumps({"data":"Error","error":Board.ErrorMessage}),
                    status=300,
                    mimetype='application/json'
                )
        print(response)
        return response


class disCard(Resource):
    def post(self):
        global Board
        global started
        if started == False:
            response = app.response_class(
                response=json.dumps({"data":"game is not started"}),
                status=Board.ErrorMessage,
                mimetype='application/json'
            )
        else:
            playerID = request.form.get("playerID")
            cardListID = request.form.get("cardListID")
            cardID = request.form.get("cardID")
            for ID in cardListID:
                if board.PlayCard(Board, ID, PlayerID) == True:
                    response = app.response_class(
                        response=json.dumps({"data":"error"}),
                        status=Board.ErrorMessage,
                        mimetype='application/json'
                    )
                    return response

            if Board.CardDrawList == []:
                Board.CardDrawList = Board.CardDiscardList
                random.shuffle(Board.CardDrawList)
                CardDiscardList = []
            Board.CardDiscardList.append(cardID)
            cardDraw = Board.CardDrawList[0]
            Board.CardDrawList.pop(0)
            response = app.response_class(
                response=json.dumps({"data":cardDraw}),
                status=Board.ErrorMessage,
                mimetype='application/json'
            )
            return response

class addUsers(Resource):
    def post(self):
        global started
        if started == True:
            response = app.response_class(
                response=json.dumps({"data":"game is started"}),
                status=300,
                mimetype='application/json'
            )
        else:
            user = request.form.get("name")
            if checkUserName(user) == False:
                response = app.response_class(
                    response=json.dumps({"data":"name already taken"}),
                    status=300,
                    mimetype='application/json'
                )
            else:
                addUserToParty(user)
                response = app.response_class(
                    response=json.dumps({"data":playerList}),
                    status=200,
                    mimetype='application/json'
                )
        return response

def getNextCard():
    global Board
    card = Board.CardDrawList[0]
    Board.CardDrawList.pop(0)
    return card

class userAfk(Resource):
    def get(self):
        global started
        
        id = request.headers.get("playerID")
        getCard = request.headers.get("getCard")
        result = setId(id)
        if getCard == 'True' and started == True:
            card1 = getNextCard()
            card2 = getNextCard()
            card3 = getNextCard()
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started, "card1": card1, "card2": card2, "card3": card3}),
                status=result,
                mimetype='application/json'
            )
        else:
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started}),
                status=result,
                mimetype='application/json'
            )
        return response

class startGame(Resource):
    def get(self):
        global Board
        global started
        Board = board.getBoard(4, idList)
        started = True
        print("Done")
        response = app.response_class(
            status=300,
            mimetype='application/json'
        )
        return response


api.add_resource(playCard, '/playCard')
api.add_resource(disCard, '/disCard')
api.add_resource(addUsers, '/addUsers')
api.add_resource(userAfk, '/userAfk')
api.add_resource(startGame, '/startGame')

def setId(id):
    for x in idList:
        if id == x["id"]:
            x.update({"isHere":True})
            return 200
    return 300

def updatePlayer():
    i = 0
    for x in idList:
        print(i, "   ", x["id"])
        if x["id"] == 0 and i < 5:
            while i < 5 and idList[i + 1]["id"] != 0:
                print("lol")
                idList[i].update({"id":idList[i + 1]["id"]})
                idList[i].update({"isHere":idList[i + 1]["isHere"]})
                idList[i + 1].update({"isHere":False})
                idList[i].update({"id":0})
                i += 1
            break
        i += 1

def checkAFK():
    while afkWile == True:
        print("\n idList \n")
        print(idList)
        print("\n")
        for x in idList:
            if x["id"] != 0:
                if x["isHere"] == True:
                    x.update({"isHere":False})
                else:
                    x.update({"id":0})
                    if started == False:
                        updatePlayer()
        print("\n update player \n")
        print(idList)
        print("\n")
        time.sleep(20)


def checkUserName(name):
    for x in playerList:
        if x["name"] == name:
            return False
    return True

def addUserToParty(name):
    id = randrange(1000000000)
    for x in playerList:
        if x["id"] == 0:
            x.update({"id":id,"name":name})
            break
    for y in idList:
        if y["id"] == 0:
            y.update({"id":id, "isHere":True})
            break

def test2():
    global Board
    #print(Board.PlayerList)

def test():
    global Board
    Board = board.getBoard(4, idList)
    #print("lol")
    #print(Board.BoardGame)
    #print(Board.BoardGame)

if __name__ == '__main__':
    test()
    app.run(port=4004, debug=True)
    #p1 = Process(target=checkAFK)
    #p1.start()
    #p1.join()
