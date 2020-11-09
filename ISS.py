from sense_hat import SenseHat
sense=SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        if event.action=='pressed':
            sense.clear()
            if event.direction=='up':
                temp=sense.get_temperature()
                temp=round(temp,2)
                print(temp)
                sense.show_message(str(temp))
                #inputs stack up and output all at once after
                #idk how to clear message partway through
            elif event.direction=='left':
                pres=sense.get_pressure()
                pres=round(pres,2)
                print(pres)
                sense.show_message(str(pres))
            elif event.direction=='right':
                humid=sense.get_humidity()
                humid=round(humid,2)
                print(humid)
                sense.show_message(str(humid))