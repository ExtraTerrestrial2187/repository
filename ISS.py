from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
colour=(0,0,0)
while True:
    for event in sense.stick.get_events():
        if event.action=='pressed':
            sense.clear()
            if event.direction=='up':
                temp=sense.get_temperature()
                temp=round(temp,2)
                if temp > 20 or temp < 28 :
                    colour=(255,0,0)
                else:
                    colour=(0,255,255)
                print(temp)
                sense.show_message(str(temp),text_colour=colour)
                #inputs stack up and output all at once after
                #idk how to clear message partway through
            elif event.direction=='left':
                pres=sense.get_pressure()
                pres=round(pres,2)
                if pres !=1013:
                    colour=(255,0,0)
                else:
                    colour=(0,255,255)
                print(pres)
                sense.show_message(str(pres),text_colour=colour)
            elif event.direction=='right':
                humid=sense.get_humidity()
                humid=round(humid,2)
                if humid >58 or humid <62 :
                    colour=(255,0,0)
                else:
                    colour=(0,255,255)
                print(humid)
                sense.show_message(str(humid),text_colour=colour)