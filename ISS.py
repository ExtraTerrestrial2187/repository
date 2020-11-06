from sense_hat import SenseHat
sense=SenseHat()
sense.clear()

while True:
    temp=sense.get_temperature()
    temp=round(temp,2)
    print(temp)
    sense.show_message(str(temp))
    
# stick code
#sense.stick.direction_up=red
#sense.stick.direction_down=blue
#sense.stick.direction_right=yellow
#sense.stick.direction_left=green