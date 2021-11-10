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
        "id":0,
        "isHere":False,
        "playTurn":False
    },
    {
        "id":0,
        "isHere":False,
        "playTurn":False
    },
    {
        "id":0,
        "isHere":False,
        "playTurn":False
    },
    {
        "id":0,
        "isHere":False,
        "playTurn":False
    },
    {
        "id":0,
        "isHere":False,
        "playTurn":False
    },
    {
        "id":0,
        "isHere":False,
        "playTurn":False
    },
]

playerList = [
    {
        "id":0,
        "name":"",
        "color":"rouge"
    },
    {
        "id":0,
        "name":"",
        "color":"bleu"
    },
    {
        "id":0,
        "name":"",
        "color":"vert"
    },
    {
        "id":0,
        "name":"",
        "color":"jaune"
    },
    {
        "id":0,
        "name":"",
        "color":"orange"
    },
    {
        "id":0,
        "name":"",
        "color":"violet"
    },
]

class playCard(Resource):
    def post(self):
        print("idList: ", idList)
        global Board
        global started
        started = True
        if started == False:
            response = app.response_class(
                response=json.dumps({"data":"Error","Message":"La partie n'est pas commencé","status":300}),
                status=300,
                mimetype='application/json'
            )
        else:
            value1 = request.form.get("value1")
            value2 = request.form.get("value2")
            valueList = request.form.get("valueList")
            playerID = request.form.get("playerID")
            cardID = request.form.get("cardID")
            print("playerID: ", playerID)
            print("acrd id: ", cardID)
            if checkTurn(playerID) == False:
                response = app.response_class(
                    response=json.dumps({"data":"Error", "Message":"Ce n'est pas votre tour de jouer","status":300}),
                    status=300,
                    mimetype='application/json'
                )
                return response
            Board = board.PlayCard(Board, cardID, value1, value2, valueList, playerID)
            print(Board.ErrorMessage)
            if Board.Status == True:
                print("pd1")
                if Board.CardDrawList == []:
                    Board.CardDrawList = Board.CardDiscardList
                    random.shuffle(Board.CardDrawList)
                    CardDiscardList = []
                Board.CardDiscardList.append(int(cardID))
                cardDraw = Board.CardDrawList[0]
                Board.CardDrawList.pop(0)
                updateTurn()
                response = app.response_class(
                    response=json.dumps({"data":cardDraw, "Message":Board.ErrorMessage,"status":200}),
                    status=200,
                    mimetype='application/json'
                )
            else:
                print("pd2")
                response = app.response_class(
                    response=json.dumps({"data":"Error","Message":Board.ErrorMessage,"status":300}),
                    status=300,
                    mimetype='application/json'
                )
        print(response)
        return response


class disCard(Resource):
    def post(self):
        global Board
        global started
        started = True
        if started == False:
            print("salut1")
            response = app.response_class(
                response=json.dumps({"data":"Error","Message":"La partie n'est pas commencé","status":300}),
                status=300,
                mimetype='application/json'
            )
        else:
            playerID = request.form.get("playerID")
            cardID = request.form.get("cardID")
            card1 = request.form.get("card1")
            card2 = request.form.get("card2")
            card3 = request.form.get("card3")
            valueList = []
            if checkTurn(playerID) == False:
                response = app.response_class(
                    response=json.dumps({"data":"Error", "Message":"Ce n'est pas votre tour de jouer","status":300}),
                    status=300,
                    mimetype='application/json'
                )
                return response
            ##cardListID = request.form.get("cardListID")
            ##cardID = request.form.get("cardID")
            if board.GlobalCheckCard(Board, card1, playerID) == True:
                valueList.append(card1)
            if board.GlobalCheckCard(Board, card2, playerID) == True:
                valueList.append(card2)
            if board.GlobalCheckCard(Board, card3, playerID) == True:
                valueList.append(card3)

            if valueList != []:
                print("salut2")
                response = app.response_class(
                    response=json.dumps({"data":valueList, "Message": "Une ou plusieurs cartes sont jouables","status":300}),
                    status=300,
                    mimetype='application/json'
                )
                return response

            if Board.CardDrawList == []:
                Board.CardDrawList = Board.CardDiscardList
                random.shuffle(Board.CardDrawList)
                CardDiscardList = []
            Board.CardDiscardList.append(int(cardID))
            cardDraw = Board.CardDrawList[0]
            Board.CardDrawList.pop(0)
            updateTurn()
            print("salut3")
            response = app.response_class(
                response=json.dumps({"data":cardDraw, "Message":"La carte a été corectement jeté","status":202}),
                status=202,
                mimetype='application/json'
            )
            return response

class addUsers(Resource):
    def post(self):
        global started
        if started == True:
            response = app.response_class(
                response=json.dumps({"data":"Error", "Message": "La partie a déja commencé","status":300}),
                status=300,
                mimetype='application/json'
            )
            return response
        if playerList[5]["id"] != 0:
            response = app.response_class(
                response=json.dumps({"data":"Error", "Message": "La partie est pleine","status":300}),
                status=300,
                mimetype='application/json'
            )
            return response
        else:
            user = request.form.get("name")
            if checkUserName(user) == False:
                response = app.response_class(
                    response=json.dumps({"data":"Error", "Message":"Ce nom est déja utilisé","status":300}),
                    status=300,
                    mimetype='application/json'
                )
            else:
                addUserToParty(user)
                response = app.response_class(
                    response=json.dumps({"data":playerList, "Message":"Le joueur a été ajouté","status":200}),
                    status=200,
                    mimetype='application/json'
                )
            return response

class userAfk(Resource):
    def post(self):
        global started

        id = int(request.form.get("playerID"))
        getCard = request.form.get("getCard")
        print("getCard: ", getCard)
        print("gettypeCard: ", type(getCard))
        result = setId(id)
        if result == 300:
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started, "status":result}),
                status=result,
                mimetype='application/json'
            )
            return response
        print("getCard: ", getCard)
        if getCard == 'true' and started == True:
            print("je suis la")
            card1 = getNextCard()
            card2 = getNextCard()
            card3 = getNextCard()
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started, "card1": card1, "card2": card2, "card3": card3,"status":result}),
                status=result,
                mimetype='application/json'
            )
            return response
        else:
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started,"status":result}),
                status=result,
                mimetype='application/json'
            )
            return response

class startGame(Resource):
    def get(self):
        global Board
        global started
        idList[0].update({"playTurn":True})
        print(getIdLength(idList))
        Board = board.getBoard(getIdLength(idList), idList)
        if Board.Status == 300:
            response = app.response_class(
                response=json.dumps({"data":playerList, "started": started,"status":Board.Status, "Message": Board.ErrorMessage}),
                status=300,
                mimetype='application/json'
            )
            return response
        else:
            started = True
            print("Done")
            response = app.response_class(
                status=200,
                mimetype='application/json'
            )
            return response


api.add_resource(playCard, '/playCard')
api.add_resource(disCard, '/disCard')
api.add_resource(addUsers, '/addUsers')
api.add_resource(userAfk, '/userAfk')
api.add_resource(startGame, '/startGame')

def getIdLength(idList):
    i = 0
    for x in idList:
        if x["id"] == 0:
            break
        i += 1
    return i

def checkTurn(playerID):
    print("id: ", playerID)
    playerID = int(playerID)
    for x in idList:
        if x["id"] == playerID:
            print("ici: ", x["playTurn"])
            return x["playTurn"]
    return False

def updateTurn():
    for i in range(len(idList)):
        if idList[i]["playTurn"] == True:
            if i == 5 or idList[i + 1]["id"] == 0:
                idList[0].update({"playTurn":True})
            else:
                idList[i + 1].update({"playTurn":True})
            idList[i].update({"playTurn":False})
            break



def getNextCard():
    global Board
    card = Board.CardDrawList[0]
    Board.CardDrawList.pop(0)
    return card

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
