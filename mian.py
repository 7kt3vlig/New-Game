import pygame 
import os 


WIDTH, HEIGHT = 1500, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game PogChamp!")


BORDER = pygame.Rect(WIDTH//2 - 10 , 0, 20, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
BULLET_VEL = 10
MAX_BULLETS = 4
VELOCITY = 7
SHARK_WIDTH, SHARK_HEIGHT = 90, 50 

SHARK1_HIT = pygame.USEREVENT + 1 
SHARK2_HIT = pygame.USEREVENT + 2 


SHARK_1_IMAGE = pygame.image.load(os.path.join("assets", "shark1.png"))
SHARK_1 = pygame.transform.scale(SHARK_1_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))
SHARK_2_IMAGE = pygame.image.load(os.path.join("assets", "shark2.png"))
SHARK_2 = pygame.transform.scale(SHARK_2_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))





def draw_window(shark1, shark2, shark1_bullets, shark2_bullets):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(SHARK_1, (shark1.x, shark1.y))
    WIN.blit(SHARK_2, (shark2.x, shark2.y))

    for bullet in shark1_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in shark2_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

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

def handle_bullets(shark1_bullets, shark2_bullets, shark1, shark2):
    for bullet in shark1_bullets:
        bullet.x += BULLET_VEL
        if shark2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHARK1_HIT))
            shark1_bullets.remove(bullet)

    for bullet in shark2_bullets:
        bullet.x -= BULLET_VEL
        if shark1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHARK2_HIT))
            shark2_bullets.remove(bullet)

def main ():
    shark1 = pygame.Rect(100, 300, SHARK_WIDTH, SHARK_HEIGHT)
    shark2 = pygame.Rect(1300, 300, SHARK_WIDTH, SHARK_HEIGHT)

    shark1_bullets = []
    shark2_bullets = []
    clock = pygame.time.Clock()

    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LCTRL and len(shark1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(shark1.x + shark1.width, shark1.y + shark1.height//2 - 2.5, 10, 5)
                    shark1_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(shark2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(shark2.x, shark1.y + shark2.height//2 - 2.5, 10, 5)
                    shark2_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        shark1_movement(keys_pressed, shark1)
        shark2_movement(keys_pressed, shark2)


        handle_bullets(shark1_bullets, shark2_bullets, shark1, shark2)

        draw_window(shark1, shark2, shark1_bullets, shark2_bullets)

    pygame.quit()


if __name__ == "__main__":
    main()

