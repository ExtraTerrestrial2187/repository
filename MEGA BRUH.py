from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
g=(0,255,0)
x=3
y=3
sense.set_pixel(x,y,g)
while True:
    for event in sense.stick.get_events():
        if event.action=='pressed':
            if event.direction=='up':
                y=y-1
                sense.set_pixel(x,y,g)
            if event.direction=='down':
                y=y+1
                sense.set_pixel(x,y,g)
            if event.direction=='left':
                x=x-1
                sense.set_pixel(x,y,g)
            if event.direction=='right':
                x=x+1
                sense.set_pixel(x,y,g)
            if event.direction=='middle':
                sense.clear()
                x=3
                y=3
                sense.set_pixel(x,y,g)