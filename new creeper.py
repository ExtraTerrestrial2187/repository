from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
#define colours
b=(0,0,255)
B=(102,51,0)
S=(205,133,63)
W=(255,255,255)
#setup matrix variable
image_pixels=[
    B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    B,S,S,S,S,S,S,B,
    S,S,S,S,S,S,S,S,
    S,W,b,S,S,b,W,S,
    S,S,S,B,B,S,S,S,
    S,S,B,S,S,B,S,S,
    S,S,B,B,B,B,S,S,
    ]
sense.set_pixels(image_pixels)