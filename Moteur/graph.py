import arcade
import arcade.gui
import prepare
import xerox
import myconstants
from multiprocessing import Array, Process, Queue
import json
import requests
import time
import animations

class MyGame(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, q):

        # Call the parent class and set up the window
        super().__init__(myconstants.SCREEN_WIDTH, myconstants.SCREEN_HEIGHT, myconstants.SCREEN_TITLE)

        self.tile_list = None
        self.pointer_list = None
        self.pointer_id = None
        self.card_list = None
        self.player_list = None
        self.score = [0, 1, 3, 3, 4, 5]
        self.pseudo = ["Tim", "PIt", "Jack", "John", "Lee", "Spike"]
        self.turn = ""
        self.link = ""
        self.link_flag = False
        self.disp = "MENU"
        self.q = q
        self.animation = None
        self.animate = None
        self.card = None

        self.sound = arcade.load_sound("../Client_Web/src/ressources/Happy_2.wav")
        self.playing = False
        self.pan = 0.5
        self.volume = 0.5
        self.bang = arcade.Sound("../Client_Web/src/ressources/gunshot.wav")
        self.quack = arcade.Sound("../Client_Web/src/ressources/quack.wav")
        self.danse = arcade.Sound("../Client_Web/src/ressources/danse.wav")
        self.player = None
        self.dance_player = None

        self.board_list = None
        self.board = None
        self.boardTmp = None
        self.players_infos = None
        self.id_list = None
        self.players = None
        self.isUpdate = True
        self.image_x = 0
        self.image_y = 0
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        
        print("setup")
        self.score = [0, 0, 0, 0, 0, 0]
        self.pseudo = []
        self.players = []
        self.turn = "Bleu"
        self.board = []
        self.boardTmp = []
        self.players_infos = []
        self.id_list = []

        prepare.create_menu(self)
        prepare.create_lists(self)

        self.card_list = arcade.SpriteList()
        card = arcade.Sprite("../Client_Web/src/ressources/dos_carte_action.png", myconstants.POINTER_SCALING)
        card.center_x = 1188
        card.center_y = 258
        self.card_list.append(card)

        self.board_list = arcade.SpriteList()
        image_source = "../Client_Web/src/ressources/plateau.png"
        self.board = arcade.Sprite(image_source, myconstants.CHARACTER_SCALING)
        self.board.center_x = 700
        self.board.center_y = 300
        self.board_list.append(self.board)
        self.animation = arcade.SpriteList()

    def on_click_disp(self, event):
        if (self.link == ""):
            self.link = "hello there"
        else:
            self.link = ""

    def on_click_copy(self, event):
        xerox.copy(u'is tgis reealy working')
    
    def on_click_quit(self, event):
        arcade.exit()

    def on_click_start(self, event):
        r = requests.get('http://127.0.0.1:4004/startGame')
        test = json.loads(r.text)
        array = []
        if (test["status"] == 200):
            print(test["data"])
            resp = self.q.get()
            print(resp["data"])
            self.board = resp["data"]
            self.boardTmp = resp["data"]
            self.id_list = resp["idList"]
            self.players_infos = resp["playerList"]
            prepare.create_board(self)
            prepare.update_players(self)
            self.disp = "GAME"

    def parse_queu(self):
        print("///////////////////////////////////////")
        resp = self.q.get()
        print("Turn resp: ", resp)
        array = []
        if resp["type"] == "CardPlay":
            self.boardTmp = resp["data"]
            prepare.create_lists(self)
            self.players_infos = resp["playerList"]
            print("id_list: ", resp["idlist"])
            self.id_list = resp["idlist"]
            prepare.update_players(self)
            self.card = resp["card"]
            prepare.check_card(self)
            print("WILL UPDATE")
            if (self.isUpdate == True):
                print("is UPDATE PLS")
                self.board = resp["data"]
                prepare.create_board(self)
        if resp["type"] == "PlayerList":
            for i in range(0, len(resp["data"]), 1):
                print(resp["data"][i]["name"])
                array.append(resp["data"][i]["name"])
            self.pseudo = array
            self.players = resp["data"]
            myconstants.PLAYER_NBR += 1
            prepare.create_player_list(self)
        

    def on_draw(self):
        """Render the screen."""

        if (self.playing == False):
            self.player = arcade.play_sound(sound=self.sound, pan=self.pan, volume=self.volume, looping=True)
            self.playing = True
        if (self.dance_player != None and self.danse.is_complete(self.dance_player)):
            self.sound.set_volume(volume=self.volume, player=self.player)
        arcade.start_render()
        if (self.q.empty() == False):
            self.parse_queu()
        if (self.disp == "MENU"):
            self.manager.draw()
            score_text = f"{self.link}"
            arcade.draw_text(score_text, 550, 700, arcade.csscolor.WHITE, 32)
            self.player_list.draw()
            y = 770
            for i in range(0, myconstants.PLAYER_NBR, 1):
                score_text = f"{self.pseudo[i]}"
                arcade.draw_text(score_text, 42, y, arcade.csscolor.WHITE, 18)
                y -= 40

        if (self.disp == "GAME"):
            self.board_list.draw()
            self.tile_list.draw()
            self.pointer_list.draw()
            self.card_list.draw()
            self.player_list.draw()
            y = 770
            for i in range(0, myconstants.PLAYER_NBR, 1):
                score_text = f"{self.pseudo[i]} Canards morts: {self.score[i]}"
                arcade.draw_text(score_text, 42, y, arcade.csscolor.WHITE, 18)
                y -= 40
            score_text = f"C'est le tour du joueur: {self.turn}"
            arcade.draw_text(score_text, 400, 700, arcade.csscolor.WHITE, 32)
            animations.explosion(self)
            animations.doubleExplosion(self)
            animations.move_all(self)
            animations.death_move(self)
            animations.double_death_move(self)
            animations.switch_move(self)
            animations.fulguro(self)
            animations.aim(self)
            animations.doubleAim(self)
            animations.peace(self)
        # Code to draw the screen goes here


def start(q):
    """Main function"""
    window = MyGame(q)
    window.setup()
    arcade.run()