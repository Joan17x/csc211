from gasp import * 
from random import randint
begin_graphics()

finished = False
player_x = random.randint(0,63)
player_y = random.randint(0,47)
def place_player():
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    print("I'm moving..")
    update_when('key_pressed')

place_player()

while not finished:
    move_player()

end_graphics()