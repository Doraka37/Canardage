import arcade
import arcade.gui
import myconstants

link_text = ""

def create_lists(self):
    i = 0
    self.player_list = arcade.SpriteList()
    for y in range(780, 540, -40):
        if (i >= myconstants.PLAYER_NBR):
            break
        player = arcade.Sprite("../Client_Web/src/ressources/icone_canard.png", myconstants.PLAYER_SCALING)
        player.center_x = 20
        player.center_y = y
        self.player_list.append(player)
        i += 1

    self.tile_list = arcade.SpriteList()
    for x in range(210, 1134, 162):
        tile = arcade.Sprite("../Client_Web/src/ressources/icone_canard.png", myconstants.TILE_SCALING)
        tile.center_x = x
        tile.center_y = 250
        self.tile_list.append(tile)

    self.pointer_list = arcade.SpriteList()
    for x in range(213, 1147, 162):
        pointer = arcade.Sprite("../Client_Web/src/ressources/Jeton_Cible.png", myconstants.POINTER_SCALING)
        pointer.center_x = x
        pointer.center_y = 395
        self.pointer_list.append(pointer)
    return self

def create_menu(self):

    display_button = arcade.gui.UIFlatButton(text="Afficher l'url", width=200)
    self.v_box.add(display_button.with_space_around(bottom=20))
    display_button.on_click = self.on_click_disp

    copy_button = arcade.gui.UIFlatButton(text="Copier l'url", width=200)
    self.v_box.add(copy_button.with_space_around(bottom=20))
    copy_button.on_click = self.on_click_copy

    start_button = arcade.gui.UIFlatButton(text="Lancer la partie", width=200)
    self.v_box.add(start_button.with_space_around(bottom=20))
    start_button.on_click = self.on_click_start

    quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
    self.v_box.add(quit_button.with_space_around(bottom=20))
    quit_button.on_click = self.on_click_quit

    self.link = link_text

    self.manager.add(
    arcade.gui.UIAnchorWidget(
        anchor_x="center_x",
        anchor_y="center_y",
        child=self.v_box)
    )