from gasp import *

begin_graphics()

Circle((100, 400), 40)

for x in 85, 115:
    Circle((x, 415), 5)
    
Line((95, 395), (100, 415))

Line((95, 395), (110, 395))

Arc((100, 405), 30, 225, 315)


for x in range(75,100,5):
    Arc((x,415), 30, -225, -315)


Arc((60,400), 10, 90, 270)
Arc((140, 400), 10, -90, 100)

Line((75, 420),(80, 425))
Line((80, 425), (90, 425))
Line((125, 420), (120, 425))
Line((120, 425), (110, 425))

update_when('key_pressed')
end_graphics()
