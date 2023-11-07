import hal.hal_input_switch as switch
import hal.hal_led as led
from time import sleep

led.init()
switch.init()

#Exercise 2 part b
# while(1):
#     if switch.read_slide_switch():
#         led.set_output(0,1)
#         sleep(0.1)
#         led.set_output(0,0)
#         sleep(0.1)

#     else:
#         led.set_output(0,0)


#Exercise 2 part c
# while(1):
#     if switch.read_slide_switch():
#         led.set_output(0,1)
#         sleep(0.05)
#         led.set_output(0,0)
#         sleep(0.05)

#     else:
#         led.set_output(0,1)
#         sleep(0.1)
#         led.set_output(0,0)
#         sleep(0.1)
       

#Exercise 2 part d

while(1): #left
    if switch.read_slide_switch():
        led.set_output(0,1)
        sleep(0.1)
        led.set_output(0,0)
        sleep(0.1)

    else: #right
        for i in range(50):
            led.set_output(0,1)
            sleep(0.05)
            led.set_output(0,0)
            sleep(0.05)
        
        while switch.read_slide_switch() == 0:
            led.set_output(0,0)

            
   

        
       
       