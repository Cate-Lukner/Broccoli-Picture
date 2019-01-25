"""
This code is intended to draw a picture of a beautiful 
piece of broccoli that all vegans can admire, but the
omnivores may scoff at. 
"""
# import the 'arcade' and 'random' libraries
import arcade
import random

# Opens 600x600 window titled 'Beautiful Broccoli'
arcade.open_window(600, 600, 'Beautiful Broccoli')

# Get ready to draw
arcade.start_render()

# --- Draw the table ---

# draws the wood of the table
texture = arcade.load_texture("images/wood.jpg")
arcade.draw_texture_rectangle(
    300, 300, 600,
    600, texture
    )

# draws the red and white tablecloth
texture = arcade.load_texture("images/tablecloth.jpg")
scale = 0.6
arcade.draw_texture_rectangle(
    300, 300, scale * texture.width,
    scale * texture.height, texture
    )


# --- Draw the plate ---

# shading around the plate
arcade. draw_circle_filled(300, 300, 205, (0, 0, 0, 90))

# creates the white plate with an inner circle of slightly
# different white
arcade.draw_circle_filled(300, 300, 200, arcade.color.WHITE)
arcade.draw_circle_filled(300, 300, 150, (250, 250, 250))

# outer outline of the plate
arcade.draw_circle_outline(300, 300, 200, arcade.color.BLACK, 3)

# inner outline of the plate
arcade.draw_circle_outline(300, 300, 150, arcade.color.BLACK, 3)

# shading for inner plate
arcade.draw_circle_outline(300, 300, 147, (0, 0, 0, 90), 3)


# --- Draw the Broccoli ---

# shading for the broccoli
arcade.draw_circle_filled(330, 320, 45, (0, 0, 0, 5))
arcade.draw_ellipse_filled(
    290, 300, 45, 35,
    (0, 0, 0, 5), 30)

# creates broccoli stem with 'texture' of a broccoli stem
broccoli_texture = arcade.load_texture("images/broccoli_stem.jpg")
arcade.draw_texture_rectangle(
    280, 295, 45, 30, 
    broccoli_texture, 30 
    )

# creates random circles of color green that will fill up
# the broccoli "branches"
def broccoli_branches(color):
    for i in range (0, 5):
        x = random.randint(290, 340)
        y = random.randint(290, 340)
        arcade.draw_circle_filled(x, y, 6, color)

# uses broccoli_branches function with different colors
# of green to create different colored circles as the
# broccoli branches
for i in range(0, 5):
    broccoli_branches((123, 179, 109))
    broccoli_branches((57, 130, 39))
    broccoli_branches((21, 89, 4))
    broccoli_branches((69, 112, 58))
    broccoli_branches((57, 84, 50))
    broccoli_branches((36, 97, 20))


# --- Draw the text ---
arcade.draw_text(
    "Oh, what beautiful broccoli!",
    60, 10,
    arcade.color.BLACK, 30
    )


# --- Finish drawing ---
arcade.finish_render()

# keeps window up until user closes it
arcade.run()