import pygame
import random


state = False
nome = input('Nome: ')
email = input('Email: ')
log = open('log.txt','a')
log.write(f'Nome: {nome}\nEmail: {email}\n')
log.close()
state = True

pygame.init()
altura = 480
largura = 854
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("PacMan")
bg = pygame.image.load("assets/background.png")

gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

icone = pygame.image.load("assets/pacman2.ico")
pygameDisplay.set_icon(icone)

def main():
    jogando = True
    movimentoX = random.randrange(0, largura)
    movimentoY = 0
    fantasma = pygame.image.load("assets/fantasma1.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    while True:
        
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if jogando == True:
            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(fantasma, (movimentoX, movimentoY))

        pygameDisplay.update()
        clock.tick(60)

main()