import arcade
import myconstants
import prepare

def animation_handler(self):
    print("ok")

def explosion(self):
    if (self.animate == "Explosion"):
        self.animation = arcade.SpriteList()
        tmpSprite = arcade.Sprite(myconstants.PATH + "explosion.png", 3, self.image_x, self.image_y, 100, 100)
        tmpSprite.center_x = (48 + (int(self.card["value1"]) * 162))
        tmpSprite.center_y = 250
        self.animation.append(tmpSprite)
        self.image_x += 100
        if (self.image_x >= 1000):
            self.image_x = 0
            self.image_y += 100
            if (self.image_y >= 800):
                self.animate = "MoveFrom"
                self.image_x = 0
                self.image_y = 0
        self.animation.draw()

def move_all(self):
    if (self.animate == "MoveAll"):
        for i in range(0, myconstants.BOARD_SIZE, 1):
            self.tile_list[i].center_x -= 3
    if (self.tile_list[0].center_x <= 48):
        self.animate = ""
        self.isUpdate = True
        prepare.create_board(self)

def death_move(self):
    if (self.animate == "MoveFrom"):
        val = int(self.card["value1"])
        if (val == 6):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)
            return
        if (self.board[val - 1]["duck"] == "empty"):
            self.animate = ""
            self.isUpdate = True
            return
        if (self.card["value2"] == '0'):
            print("bonjour")
            dead = 0
            self.tile_list[(val - 1)].center_y = -2000
        else:
            dead = 1
            self.tile_list[(val - 1)].center_y = -2000
        for i in range(val + dead, myconstants.BOARD_SIZE, 1):
            self.tile_list[i].center_x -= 3
        if (self.tile_list[val].center_x <= (48 + val * 162)):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)

def switch_move(self):
    if (self.animate == "SwitchLeft"):
        print("SwitchLeft")
        val = int(self.card["value1"])
        self.tile_list[val - 1].center_x -= 3
        self.tile_list[val - 2].center_x += 3
        if (self.tile_list[val - 1].center_x <= (48 + (val -1) * 162)):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)

    if (self.animate == "SwitchRight"):
        print("SwitchRight")
        val = int(self.card["value1"])
        self.tile_list[val - 1].center_x += 3
        self.tile_list[val].center_x -= 3
        if (self.tile_list[val - 1].center_x >= (48 + (val + 1) * 162)):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)
