import pygame 
import os 


WIDTH, HEIGHT = 1500, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game PogChamp!")

WHITE = (255,255,255)

FPS = 60
SHARK_WIDTH, SHARK_HEIGHT = 90, 50 
SHARK_1_IMAGE = pygame.image.load(os.path.join("assets", "shark1.png"))
SHARK_1 = pygame.transform.scale(SHARK_1_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))
SHARK_2_IMAGE = pygame.image.load(os.path.join("assets", "shark2.png"))
SHARK_2 = pygame.transform.scale(SHARK_2_IMAGE, (SHARK_WIDTH, SHARK_HEIGHT))




def draw_window(shark1, shark2):
    WIN.fill(WHITE)
    WIN.blit(SHARK_1, (shark1.x, shark1.y))
    WIN.blit(SHARK_2, (shark2.x, shark2.y))

    pygame.display.update()


def main ():
    shark1 = pygame.rect(100, 300, SHARK_WIDTH, SHARK_HEIGHT)
    shark2 = pygame.rect(1300, 300, SHARK_WIDTH, SHARK_HEIGHT)



    clock = pygame.time.Clock()

    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        
        draw_window(shark1, shark2)

    pygame.quit()


if __name__ == "__main__":
    main()

