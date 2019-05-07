import serial
import time
import pygame
from pygame.locals import *


from pysabertooth import Sabertooth



saber1 = Sabertooth('/dev/ttyACM0', baudrate=115200, address=128, timeout=0.1)
saber2 = Sabertooth('/dev/ttyACM1', baudrate=115200, address=128, timeout=0.1)
lift =	serial.Serial('/dev/ttyACM2')
deploy = serial.Serial('/dev/ttyACM3')



# # The individual event object that is returned
# # This serves as a proxy to pygame's event object
# # and the key field is one of the strings in the button list listed below 
# # in the InputManager's constructor
# # This comment is actually longer than the class definition itself. 

# pygame.init()


# pygame.joystick.init() # main joystick device system



# try:
# 	j = pygame.joystick.Joystick(0) # create a joystick instance
# 	j.init() # init instance
# 	print 'Enabled joystick: ' + j.get_name()
# except pygame.error:
# 	print 'no joystick found.'


# while 1:
# 	for e in pygame.event.get(): # iterate over event stack
# 		print 'event : ' + str(e.type)
# 		if e.type == pygame.locals.JOYAXISMOTION: # 7
# 			x , y = j.get_axis(0), j.get_axis(1)
# 			print 'x and y : ' + str(x) +' , '+ str(y)			
# 		elif e.type == pygame.locals.JOYBALLMOTION: # 8
# 			print 'ball motion'
# 		elif e.type == pygame.locals.JOYHATMOTION: # 9
# 			print 'hat motion'
			
# 		elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
# 			print 'button down'
# 			saber1.drive(2, 100)
# 			saber1.drive(1, 100)
# 		elif e.type == pygame.locals.JOYBUTTONUP: # 11
# 			print 'button up'
# 			saber1.stop()



# jlist = [] # global joystick list




# def init():
# 	pygame.init()


# 	pygame.joystick.init() # init main joystick device system


# 	try:
# 		for n in range(pygame.joystick.get_count()): #
# 			stick = pygame.joystick.Joystick(n)
# 			jlist.append(stick) # create a joystick instance
# 			stick.init() # init instance
# 			# report joystick charateristics #
# 			print '-'*20
# 			print 'Enabled joystick: ' + stick.get_name()
# 			print 'it has the following devices :'
# 			print '--> buttons : '+ str(stick.get_numbuttons())
# 			print '--> balls : '+ str(stick.get_numballs())
# 			print '--> axes : '+ str(stick.get_numaxes())
# 			print '--> hats : '+ str(stick.get_numhats())
# 			print '-'*20
# 	except pygame.error:
# 		print 'pygame.error, no joystick found.'





# def main():


# 	init() # init pygame and joystick system


# 	while 1: # endless loop


# 		for e in pygame.event.get(): # iterate over event stack


# 			if e.type == pygame.locals.JOYAXISMOTION: # 7
# 				for j in jlist:
# 					for n in range(j.get_numaxes()):
# 						print 'moved axe num '+str(n)+' : ' + str(j.get_axis(n))
# 					print '-'*10 # separation


# 			elif e.type == pygame.locals.JOYBALLMOTION: # 8
# 				for j in jlist:
# 					for n in range(j.get_numballs()):
# 						print 'moved ball num '+str(n)+' : '+ str(j.get_ball(n))
# 					print '-'*10 # separation


# 			elif e.type == pygame.locals.JOYHATMOTION: # 9
# 				for j in jlist:
# 					for n in range(j.get_numhats()):
# 						print 'moved hat num '+str(n)+' : '+ str(j.get_hat(n))
# 					print '-'*10 # separation


# 			elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
# 				for j in jlist:
# 					for n in range(j.get_numbuttons()):
# 						if j.get_button(n) : # if this is down
# 							print 'down button num '+str(n)+' : '+ str(j.get_button(n))
# 					print '-'*10 # separation
						
# 			elif e.type == pygame.locals.JOYBUTTONUP: # 11
# 				for j in jlist:
# 					for n in range(j.get_numbuttons()):
# 						print 'up button num '+str(n)+' : '+ str(j.get_button(n))
# 					print '-'*10 # separation
# 			elif e.type == pygame.locals.JOYBUTTONDOWN:






# if __name__ == '__main__': main()








		



pygame.init()

done = False


# Initialize the joysticks
pygame.joystick.init()
    

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            saber1.stop()
            saber2.stop()
	    lift.write('!G 1 0 \n\r')
	    deploy.write('!G 1 0 \n\r')
	    lift.write('!G 2 0 \n\r')
	    deploy.write('!G 2 0 \n\r') #hopper

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    #print("Number of joysticks: {}".format(joystick_count) )

    
    # For each joystick:
    x=0
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
       # print("Joystick {}".format(i) )
        
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
       # print("Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        #print("Number of axes: {}".format(axes) )
        
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            #print("Axis {} value: {:>6.3f}".format(i, axis) )
    
            
        buttons = joystick.get_numbuttons()
       # print( "Number of buttons: {}".format(buttons) )
       

        for i in range( buttons ):
            button = joystick.get_button( i )
            #print("Button {:>2} value: {}".format(i,button) )
        
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        #print("Number of hats: {}".format(hats) )
    

        for i in range( hats ):
            hat = joystick.get_hat( i )
           # print("Hat {} value: {}".format(i, str(hat)) )
       
        #sleep(.1)
        button0=joystick.get_button(0)
        button1=joystick.get_button(1)
        button2=joystick.get_button(2)
        button3=joystick.get_button(3)
        button4=joystick.get_button(4)
        button5=joystick.get_button(5)
        button6=joystick.get_button(6)
        button7=joystick.get_button(7)
	button8=joystick.get_button(8)
	button9=joystick.get_button(9) 

        axis0 = joystick.get_axis( 0 )
        axis1 = joystick.get_axis( 1 )
        axis2 = joystick.get_axis( 2 )
        axis3 = joystick.get_axis( 3 )

        if button4==1:     #button4 (in code) button5 (on controller) is a half speed modifier
            axis0=axis0*.5
            axis1=axis1*.5
            axis2=axis2*.5
            axis3=axis3*.5


        if  .10 > axis0 > -.10:    #adds a deadzone into the joysticks to allow the joystick not to be perfectly center
            axis0
   
        if  .10 > axis1 > -.10:
            axis1=0
	    
        if  .10 > axis2 > -.10:
              axis2=0
        if  .10 > axis3 > -.10:
            axis3=0
            #lift.write('!G 2 -500 \n\r') #WRIST

        #*******This allows a tank drive system*******

        v=(1-abs(axis2))*(axis3) + axis3
        w=(1-abs(axis3))*(axis2) + axis2

        R= (v+w)/2
        L= (v-w)/2

        liftA=((axis1*127.5)+127.5)
        bucketA=((axis0*127.5)+127.5)

        
        R=R*127.5
        R=R+127.5   
        L=L*127.5
        L=L+127.5

        
        if button0==1:                    #Left drive motor half speed (button 1 on controller)
            saber1.drive(1, 100)
            saber1.drive(2, 100)
            saber2.drive(2, -100)
	    saber2.drive(1, -100)

        if button0 & button4==1:         #Left motor quarter speed(button4 (button5 on controller) is a half speed modifier)
            R=97.5
         

        if button1==1:                  #Right drive motor reverse half speed
            R=187.5
            saber1.drive(1, -100)
            saber1.drive(2, -100)
            saber2.drive(2, 100)
	    saber2.drive(1, 100)

        if button0 & button1==1:
            R=157.5
	    #deploy.write('!G 1 -500 \n\r')
	    lift.write('!G 2 -500 \n\r') #WRIST
	    #saber1.stop()
            #saber2.stop()
	if button2 & button3==1:
            R=157.5
	    #deploy.write('!G 1 -500 \n\r')
	    lift.write('!G 2 500 \n\r') #WRIST
            
        if button2==1:                   #Left motor reverse half speed
            L=187.5			 #Left
	    saber1.drive(1, -100)	#back R
	    saber2.drive(1, -100)	#back L
	    saber1.drive(2, 100)	#front L
	    saber2.drive(2, 100)	#front R
      #  if button2 & button4==1:
           # L=157.5
            
        if button3==1:                   #Right motor half speed
            L=67.5			 #Right
	    saber1.drive(2, -100)
	    saber2.drive(2, -100)
	    saber1.drive(1, 100)
	    saber2.drive(1, 100)
        if button3 & button4==1:
            L=97.5

        track=127.5

	if button4 == 1:
	    #lift.write('!G 2 500 \n\r') #WRIST
	    deploy.write('!G 2 -500 \n\r')   #hopper
	   
        
            
        if button5 ==1:                 #Preset actuator lift button
            #axis0=5                     #Lifts the top of the bot level
            #axis1=196
	    lift.write('!G 1 -500 \n\r')
	    #lift.write('!G 2 500 \n\r')
	   
	    #lift.read()
        if button5 & button4==1:        #Preset descend button
            axis0=176                   #Descends at half speed when compare to the lift
            axis1=55
            #lift.write('!G 1 -500 \n\r')
	    #lift.write('!G 2 500 \n\r')
	    #lift.read()

	if button6 == 1:                 #Gearmotor full speed retract
            #track = 0
	    deploy.write('!G 2 500 \n\r')   #hopper
        if button6 & button4==1:
            track = 64
            
        if button7 == 1:                #Gear motor full speed deploy
	    lift.write('!G 1 500 \n\r')
	    #lift.write('!G 2 -500 \n\r')
            track = 255
        if button7 & button4 ==1:
            track= 187.5
        
	if button8 == 1:
	    deploy.write('!G 1 -500 \n\r')		#ARM
	    #deploy.read()
	if button9 == 1:
	    deploy.write('!G 1 500 \n\r')		#ARM
	    #deploy.read()

	if button4 & button6 ==1:
	    lift.write('!G 2 500 \n\r') #WRIST
	

        

        test = axis0+axis1+axis2+axis3+track



#********************Debugging code**************************
        

        print"axis0:"
        print axis0
        print"axis1"
        print axis1
        print"axis2"
        print axis2
        print"axis3"
        print axis3
        print"track:"
        print track
        print"R:"
        print R
        print"L:"
        print L
        print "liftA: "
        print liftA
        

            
        #print test

#*************************************************************        
        
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # packer = struct.Struct('B B B B')
        # data = packer.pack(R,L,liftA,bucketA)      #packs the data for transmission
        # UDP_IP='192.168.1.100'
        # UDP_PORT='5005'
        # s.sendto(data, (UDP_IP , 5005 )) 
        # sleep(.1)                                 #frequency of tranmission                     
        
        
    

    

pygame.quit ()





