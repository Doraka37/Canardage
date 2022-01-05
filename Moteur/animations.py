import arcade
import myconstants
import prepare
import time

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
                self.quack.play(pan=self.pan, volume=2)
                self.animate = "MoveFrom"
                self.image_x = 0
                self.image_y = 0
        self.animation.draw()

def doubleExplosion(self):
    if (self.animate == "DoubleExplosion"):
        self.animation = arcade.SpriteList()
        tmpSprite = arcade.Sprite(myconstants.PATH + "explosion.png", 3, self.image_x, self.image_y, 100, 100)
        tmpSprite.center_x = (48 + (int(self.card["value1"]) * 162))
        tmpSprite.center_y = 250
        tmpSprite2 = arcade.Sprite(myconstants.PATH + "explosion.png", 3, self.image_x, self.image_y, 100, 100)
        tmpSprite2.center_x = (48 + (int(self.card["value2"]) * 162))
        tmpSprite2.center_y = 250
        self.animation.append(tmpSprite)
        self.animation.append(tmpSprite2)
        self.image_x += 100
        if (self.image_x >= 1000):
            self.image_x = 0
            self.image_y += 100
            if (self.image_y >= 800):
                self.quack.play(pan=self.pan, volume=2)
                self.animate = "DoubleMoveFrom"
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
        self.tile_list[(val - 1)].center_y = -2000
        for i in range(val, myconstants.BOARD_SIZE, 1):
            self.tile_list[i].center_x -= 3
        if (self.tile_list[val].center_x <= (48 + val * 162)):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)

def double_death_move(self):
    if (self.animate == "DoubleMoveFrom"):
        val = int(self.card["value1"])
        val2 = int(self.card["value2"])
        if (self.board[val - 1]["duck"] == "empty" and self.board[val2 - 1]["duck"] == "empty"):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)
            return
        if (self.board[val - 1]["duck"] == "empty"):
            self.card["value1"] = val2
            self.animate = "MoveFrom"
            return
        if (self.board[val2 - 1]["duck"] == "empty"):
            self.animate = "MoveFrom"
            return
        if (val == 6 or val2 == 6):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)
            return
        self.tile_list[(val - 1)].center_y = -2000
        self.tile_list[(val2 - 1)].center_y = -2000
        for i in range(val, myconstants.BOARD_SIZE, 1):
            self.tile_list[i].center_x -= 3
        if (self.tile_list[val].center_x <= (48 - 162 + val * 162) or self.tile_list[val2].center_x <= (48 - 162 + val2 * 162)):
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

def fulguro(self):
    if (self.animate == "Fulguro"):
        val = int(self.card["value1"])
        self.tile_list[val - 1].center_x -= (3 * (val - 1))
        for i in range(0, val - 1, 1):
            self.tile_list[i].center_x += 3
        if (self.tile_list[0].center_x >= (48 + 324)):
            self.animate = ""
            self.isUpdate = True
            prepare.create_board(self)

def aim(self):
    size = len(self.pointer_list)
    if (self.animate == "Aim"):
        self.pointer_list[size - 1].scale += 0.1
        if (self.pointer_list[size - 1].scale >= 2.5):
            self.animate = "Aim2"
    if (self.animate == "Aim2"):
        if (self.pointer_list[size - 1].scale <= 0.4):
            self.pointer_list[size - 1].scale = 0.4
            self.animate = ""
            return
        self.pointer_list[size - 1].scale -= 0.1

def doubleAim(self):
    size = len(self.pointer_list)
    if (self.animate == "DoubleAim"):
        self.pointer_list[size - 1].scale += 0.1
        self.pointer_list[size - 2].scale += 0.1
        if (self.pointer_list[size - 1].scale >= 2.5):
            self.animate = "DoubleAim2"
    if (self.animate == "DoubleAim2"):
        if (self.pointer_list[size - 1].scale <= 0.4):
            self.pointer_list[size - 1].scale = 0.4
            self.pointer_list[size - 2].scale = 0.4
            self.animate = ""
            return
        self.pointer_list[size - 1].scale -= 0.1
        self.pointer_list[size - 2].scale -= 0.1

def peace(self):
    if (self.animate == "Peace"):
        self.animation = arcade.SpriteList()
        tmpSprite = arcade.Sprite(myconstants.PATH + "sheet-peaceandlove.png", 3, self.image_x, self.image_y, 143, 287)
        tmpSprite.center_x = 700
        tmpSprite.center_y = 250
        self.animation.append(tmpSprite)
        self.animation.draw()
        time.sleep(0.2)
        self.image_x += 143
        if (self.image_x > 520):
            self.image_x = 0
            self.image_y += 287
            if (self.image_y > 288):
                self.animate = ""
                self.isUpdate = True