import pygame 
pygame.init()

HEIGHT = 500
WEIGHT = 500

display = pygame.display.set_mode((HEIGHT, WEIGHT))
background = pygame.Surface(display.get_size())
background.fill((0, 0, 0))
background = background.convert()
display.blit(background, (0,0))

ballsf = pygame.Surface((200, 200))   
pygame.draw.circle(ballsf, (125, 54, 55), (100,100),100) 
ballsf = ballsf.convert() 
display.blit(ballsf, (int(WEIGHT/2) - 100, int(HEIGHT/2) - 100))

time = pygame.time.Clock()


activation = True

FPS = 60
playtime = 0.0

while activation:
    milliseconds = time.tick(FPS)
    playtime += milliseconds/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activation = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                activation = False

    text = "FPS: {0:.2f} playtime:{1:.2f}".format(time.get_fps(), playtime)
    pygame.display.set_caption(text)

    pygame.display.flip()

pygame.quit()

print("\nThis game was played for {0:.2f} seconds".format(playtime))
