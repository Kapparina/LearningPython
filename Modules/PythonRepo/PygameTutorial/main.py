import pygame
import time
import random


WIDTH = 1000
HEIGHT = 800
BACKGROUND = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
pygame.display.set_caption("Space Dodge")


def draw(player):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()



def main():
    run = True

    player = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()