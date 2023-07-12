from gasp import *

begin_graphics()

Line((200, 100), (100, 300))

update_when('key_pressed')   # This keeps the graphics window open until
                             # you press a key.
end_graphics()
