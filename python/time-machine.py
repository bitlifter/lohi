from gpiozero import LED
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import time
import random

pinFactory_Diner = PiGPIOFactory(host='192.168.86.45') #diner pi
pinFactory_Pump = PiGPIOFactory(host='192.168.86.42') #pump pi

inPin_Pump_1 = Button(12,pin_factory=pinFactory_Pump)
inPin_Pump_2 = Button(16,pin_factory=pinFactory_Pump)
inPin_Pump_3 = Button(20,pin_factory=pinFactory_Pump)
inPin_Pump_4 = Button(21,pin_factory=pinFactory_Pump)

inPin_Diner_1 = Button(12,pin_factory=pinFactory_Diner)
inPin_Diner_2 = Button(16,pin_factory=pinFactory_Diner)
inPin_Diner_3 = Button(20,pin_factory=pinFactory_Diner)
inPin_Diner_4 = Button(21,pin_factory=pinFactory_Diner)

outPin_Pump_1 = LED(5, pin_factory=pinFactory_Pump)
outPin_Pump_2 = LED(6, pin_factory=pinFactory_Pump)
outPin_Pump_3 = LED(13, pin_factory=pinFactory_Pump)
outPin_Pump_4 = LED(19, pin_factory=pinFactory_Pump)

outPin_Diner_1 = LED(5, pin_factory=pinFactory_Diner)
outPin_Diner_2 = LED(6, pin_factory=pinFactory_Diner)
outPin_Diner_3 = LED(13, pin_factory=pinFactory_Diner)
outPin_Diner_4 = LED(19, pin_factory=pinFactory_Diner)


lastCount = 0
inputPins = [inPin_Pump_1,inPin_Pump_2,inPin_Pump_3,inPin_Pump_4,inPin_Diner_1,inPin_Diner_2,inPin_Diner_3,inPin_Diner_4]
outputPins = [outPin_Pump_1,outPin_Pump_2,outPin_Pump_3,outPin_Pump_4,outPin_Diner_1,outPin_Diner_2,outPin_Diner_3,outPin_Diner_4]
for outputPin in outputPins:
    outputPin.off()

pwm1 = {"state":0,"pins":[],"onMax":0,"onMin":0,"offMax":0,"offMin":0,"timer":0}
pwm2 = {"state":0,"pins":[],"onMax":0,"onMin":0,"offMax":0,"offMin":0,"timer":0}
pwm3 = {"state":0,"pins":[],"onMax":0,"onMin":0,"offMax":0,"offMin":0,"timer":0}
pwm4 = {"state":0,"pins":[],"onMax":0,"onMin":0,"offMax":0,"offMin":0,"timer":0}
pwm5 = {"state":0,"pins":[],"onMax":0,"onMin":0,"offMax":0,"offMin":0,"timer":0}

pwms = [pwm1,pwm2,pwm3,pwm4,pwm5]

currentTime = time.time()

while True:
    newTime = time.time()
    elapsedTime = (newTime - currentTime) * 1000
    currentTime = newTime

    count = 0

    for inputPin in inputPins:
       if inputPin.is_pressed:
           count = count + 1

    # do something based on count
    stateChanged = False
    if count != lastCount:
       # handle any transitions between state change
       stateChanged = True
       lastCount = count
       for outputPin in outputPins:
          outputPin.off()
       for pwm in pwms:
          pwm["state"] = 0

###################################### Edit this area
    if count > 6:
       # 7 or more inputs are active
       print(count)
    elif count > 5:
        # 6 inputs are active
       print(count)
    elif count > 4:
        # 5 inputs are active
       print(count)
    elif count > 3:
        # 4 inputs are active
       print(count)
    elif count > 2:
        # 3 inputs are active
        # example to turn on 2 PWM timers
       if stateChanged:
           pwm1["state"] = 1
           pwm1["pins"] = [outPin_Pump_1,outPin_Pump_3]
           pwm1["onMax"] = 2000
           pwm1["onMin"] = 1000
           pwm1["offMax"] = 250
           pwm1["offMin"] = 25

           pwm2["state"] = 1
           pwm2["pins"] = [outPin_Pump_2,outPin_Pump_4]
           pwm2["onMax"] = 500
           pwm2["onMin"] = 50
           pwm2["offMax"] = 250
           pwm2["offMin"] = 25
    elif count > 1:
        # 2 inputs are active
        # example to turn on an output and turn on a PWM timer
        if stateChanged:
           outPin_Diner_1.on()  # turn on an output

           pwm1["state"] = 1  #set pwm to state 1 to start it uo
           pwm1["pins"] = [outPin_Pump_1,outPin_Pump_3] # add the output pins to pulse
           pwm1["onMax"] = 500 # max millisedconds to stay on
           pwm1["onMin"] = 50  # min milliscondes to stay on
           pwm1["offMax"] = 250  # max milliseocnds to turn off
           pwm1["offMin"] = 25  # min millisconds to turn off
    elif count > 1:
       # 1 input is active
       # example to turn on an output
       if stateChanged:
           outPin_Diner_1.on()
##########################################################


    for pwm in pwms:
       if pwm["state"] == 1:
          #start pwm
          pwm["state"] = 2
          for pin in pwm["pins"]:
             pin.on()
          pwm["timer"] = random.randint(pwm["onMin"],pwm["onMax"])
       elif pwm["state"] == 2:
          #count up to timer
          pwm["timer"] -= elapsedTime
          if pwm["timer"] <= 0:
             pwm["state"] = 3
             for pin in pwm["pins"]:
                 pin.off()
             pwm["timer"] = random.randint(pwm["offMin"],pwm["offMax"]) 
       elif pwm["state"] == 3:
          pwm["timer"] -= elapsedTime
          if pwm["timer"] <= 0:
             pwm["state"] = 1


    print(count)

    # hang out for 100 milli seconds
    sleep(100/1000)

