import pygame 
import os 


WIDTH, HEIGHT = 1500, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game PogChamp!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

VELOCITY = 7

BORDER = pygame.Rect(WIDTH/2 - 10 , 0, 20, HEIGHT)




SHARK_WIDTH, SHARK_HEIGHT = 90, 50 
SHARK_1_IMAGE = pygame.image.load(os.path.join("assets", "shark1.png"))
SHARK_1 = pygame.transform.scale(SHARK_1_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))
SHARK_2_IMAGE = pygame.image.load(os.path.join("assets", "shark2.png"))
SHARK_2 = pygame.transform.scale(SHARK_2_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))

def draw_window(shark1, shark2):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SHARK_1, (shark1.x, shark1.y))
    WIN.blit(SHARK_2, (shark2.x, shark2.y))

    pygame.display.update()



def shark1_movement(keys_pressed, shark1):
    if keys_pressed[pygame.K_a] and shark1.x - VELOCITY > 0: #left key 
        shark1.x -= VELOCITY
    if keys_pressed[pygame.K_d] and shark1.x + VELOCITY + shark1.width < BORDER.x: #right key            
        shark1.x += VELOCITY
    if keys_pressed[pygame.K_w] and shark1.y - VELOCITY > 0: #up key 
        shark1.y -= VELOCITY
    if keys_pressed[pygame.K_s] and shark1.y + VELOCITY + shark1.height < HEIGHT: #down key            
        shark1.y += VELOCITY

def shark2_movement(keys_pressed, shark2):
    if keys_pressed[pygame.K_LEFT] and shark2.x - VELOCITY > BORDER.x + BORDER.width : #left key 
        shark2.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and shark2.x + VELOCITY + shark2.width < WIDTH: #right key            
        shark2.x += VELOCITY
    if keys_pressed[pygame.K_UP] and shark2.y - VELOCITY > 0: #up key 
        shark2.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and shark2.y + VELOCITY + shark2.height < HEIGHT: #down key            
        shark2.y += VELOCITY

def main ():
    shark1 = pygame.Rect(100, 300, SHARK_WIDTH, SHARK_HEIGHT)
    shark2 = pygame.Rect(1300, 300, SHARK_WIDTH, SHARK_HEIGHT)



    clock = pygame.time.Clock()

    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        shark1_movement(keys_pressed, shark1)
        shark2_movement(keys_pressed, shark2)
        draw_window(shark1, shark2)

    pygame.quit()


if __name__ == "__main__":
    main()

