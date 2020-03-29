import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
screen.fill(white)
         #Шаблоны
# pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)
# pygame.draw.circle(screen, pink, (320,240), 100, 100)
# pygame.draw.rect(screen, blue, (x,y,width,height), thickness)
# pygame.draw.arc(screen, red, (x,y,width,height), start_angle, stop_angle, thickness)
# pygame.draw.polygon(screen, green, [(270,150),(320,20),(370,150)])

#1
# pygame.draw.circle(screen, pink, (320,240), 100, 100)

#3 ANSWER no
# pygame.draw.polygon(screen, green,((200,200),(275,200),(300,100),(325,200),(400,200),(345,250),(375,350),(300,275),(225,350),(255,250)))
# pygame.draw.aalines(screen, green, True, [(200,200),(275,200),(300,100),(325,200),(400,200),(345,250),(375,350),(300,275),(225,350),(255,250)]) 
# pygame.draw.lines(screen, green, False, [(200,200),(275,200),(300,100),(325,200),(400,200),(345,250),(375,350),(300,275),(225,350),(255,250),(200,200)], 1)

#4
# pygame.draw.arc(screen, black,(0,0,2560/2,1920/2),0, 2*3.14, 1)
# pygame.draw.lines(screen, green, False, [(0,480),(640,0)])

#5
# for point in range(0,641,64): # range(start, stop, step)
#    pygame.draw.line(screen, red, (0,0), (640, point), 1)
#    pygame.draw.line(screen, red, (0,0), (point, 480), 1)

#6
# for point in range(0,256,10): # range(start, stop, step)
#    pygame.draw.line(screen, (0,point,point), (0,0), (640, point), 1)
#    pygame.draw.line(screen, (point,0,point), (0,0), (point, 480), 1)


clock = pygame.time.Clock()

running = True

FPS= 30 
playtime = 0.0

while running:
    milliseconds = clock.tick(FPS) # do not go faster than this framerate
    playtime += milliseconds / 1000.0 # add seconds to playtime 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # user pressed ESC
    text = "FPS {0}".format(FPS) +" Playtime : {0:.2f}" .format(playtime)   
    pygame.display.set_caption(text)   
    pygame.display.flip()

pygame.display.update()