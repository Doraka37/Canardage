import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)
arcade.finish_render()
arcade.run()
