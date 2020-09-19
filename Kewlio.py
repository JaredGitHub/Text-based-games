#Importing and initializing pygame and random
import pygame
import random
pygame.init()

w = pygame.display.set_mode([1500,1000])
w.fill((0,0,0))

l_leg_start = 25
r_leg_start = 150
leg_offset = 0
leg_speed = 4
l_arm_start = 100
r_arm_start = 250
arm_offset = 0
arm_speed = 3

#While loop for animating
animating = True
while animating == True:
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
            
    #Random colors
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r,g,b)
    #Random locations for circle, square and ellipse
    circle_x = random.randint(0,1500)
    circle_y = random.randint(0,1000)
    
    square_x = random.randint(0,1500)
    square_y = random.randint(0,1000)
    rect = pygame.Rect(square_x, square_y, random.randint(1,250),random.randint(1,250))
    
    circle_loc = (circle_x,circle_y)
    square_loc = (square_x,square_y)
    
    #Draw the shapes
    pygame.draw.circle(w,color,circle_loc,random.randint(1,250))
    pygame.draw.rect(w,color,rect)
    
    pygame.draw.circle(w,(0,0,0),(750,500),325)
    
    
    ####----STICK FIGURE DANCING-----####
    ###                              ####
    ###                              ####
    ###                              ####
    ###                              ####

    
    pygame.draw.circle(w, color, (750, 300), 100, 25)
    pygame.draw.line(w, color, (750, 500), (750, 390),20)


    #### ---- LEGS ---- ####

    # Instead of random values, assign each variable
    # the matching start leg variable plus leg offset
    left_leg = random.randint(500, 700)
    right_leg = random.randint(750, 1000)

    leg_offset += leg_speed

    if leg_offset > 400 or leg_offset < 0:
        leg_speed = leg_speed * -1


   
    pygame.draw.line(w, color, (750, 500), (right_leg, 700),20)
    pygame.draw.line(w, color, (750, 500), (left_leg, 700),20)


    #### ---- ARMS ---- ####
    left_arm = random.randint(350, 800)
    right_arm = random.randint(350, 800)

    # Increment arm_offset by arm_speed
    # ---> TEST AFTER THIS LINE <--- #
    arm_offset += arm_speed

    # If arm_offset is more than 200, assign it 200 and
    # multiply arm_speed by -1 (and re-assign)
    # ---> TEST AFTER THIS LINE <--- #
    if arm_offset > 200:
        arm_offset = 200
        arm_speed *= -1



    # Elif arm_offset is less than 25, assign it 25 and
    # multiply arm_speed by -1 (and re-assign)
    # ---> TEST AFTER THIS LINE <--- #
    elif arm_offset < 25:
        arm_offset = 25
        arm_speed *= -1



    # Replace the two lines below with one line: draw a
    # black line from (25, left_arm) to (275, right_arm)
    # ---> TEST AFTER THIS LINE <--- #
    pygame.draw.line(w, color, (600, left_arm), (750, 430),20)
    pygame.draw.line(w, color, (900, right_arm), (750, 430),20)

    
    
    pygame.display.flip()
    pygame.time.wait(20)
	


