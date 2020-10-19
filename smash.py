from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
#define colours
w=(0,0,0)
b=(255,255,255)
#setup matrix variable
image_pixels=[
    b,b,b,w,w,w,b,b,
    b,w,b,w,w,w,w,b,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    b,b,b,b,b,b,b,b,
    b,w,b,w,w,w,w,b,
    b,b,b,w,w,w,b,b,
    ]
sense.set_pixels(image_pixels)