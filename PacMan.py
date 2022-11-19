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
bg_perdeu = pygame.image.load("assets/over.png")

gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()

icone = pygame.image.load("assets/pacman2.ico")
pygameDisplay.set_icon(icone)

white = (255, 255, 255)
green = (34,139,34)
red = (255,0,0)

def perdeu(pontos):
    gameDisplay.blit(bg_perdeu, (0,0))
    pygame.mixer.music.stop()
    fonte = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Você obteve "+str(pontos) +" pontos!", True, green)
    gameDisplay.blit(texto, (520, 90))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 20)
    textoContinue = fonteContinue.render("press enter to restart", True, green)
    gameDisplay.blit(textoContinue, (560,115))

    pygameDisplay.update()

def main():
    jogando = True
    rightPress = False
    leftPress = False
    movimentoX = random.randrange(0, largura)
    movimentoY = 0
    velocidade = 1
    direcao = True
    posicaoXPlayer = 400
    posicaoYPlayer = 378
    movimentoXPlayer = 0
    boneco = pygame.image.load("assets/pacman.png")
    fantasma = pygame.image.load("assets/fantasma1.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    larguraPlayer = 65
    velocidadePlayer = 15
    pontos = 0
    pontosMorte = 0

    while True:
           
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftPress = True
                elif event.key == pygame.K_RIGHT:
                    rightPress = True
                elif event.key == pygame.K_RETURN:
                    main()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftPress = False
                elif event.key == pygame.K_RIGHT:
                    rightPress = False

        if jogando == True:

            movimentoXPlayer = 0
            if rightPress:
                movimentoXPlayer = velocidadePlayer
            if leftPress:
                movimentoXPlayer = -velocidadePlayer

            #controlar limites do boneco
            posicaoXPlayer = posicaoXPlayer + movimentoXPlayer
            if posicaoXPlayer < 0:
                posicaoXPlayer = 0
            elif posicaoXPlayer > largura - larguraPlayer:
                posicaoXPlayer = largura - larguraPlayer

            gameDisplay.blit(bg, (0,0))
            gameDisplay.blit(boneco, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(fantasma, (movimentoX, movimentoY))

            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 25))

            fonteMorte = pygame.font.Font('freesansbold.ttf', 20)
            pontosMortetxt = fonteMorte.render("Erros: "+str(pontosMorte), True, red)
            gameDisplay.blit(pontosMortetxt, (130, 25))

            # movimento do fantasma
            if direcao == True:
                if movimentoY <= 480 - 68:
                    movimentoY = movimentoY + velocidade
                else:
                    movimentoY = 0
                    movimentoX = random.randrange(0, largura)
                    velocidade = velocidade + 0.4
                    pontosMorte += 1
                    if pontosMorte == 3:
                        perdeu(pontos)
                        jogando = False
                    else:    
                        direcao = True
        
        #colisão do fantasma com o personagem    
        bonecoRect = boneco.get_rect()
        bonecoRect.x = posicaoXPlayer
        bonecoRect.y = posicaoYPlayer   

        fantasmaRect = fantasma.get_rect()
        fantasmaRect.x = movimentoX
        fantasmaRect.y = movimentoY

        if fantasmaRect.colliderect(bonecoRect) == True:
            movimentoY = 0
            movimentoX = random.randrange(0, largura)
            velocidade = velocidade + 0.4
            direcao = True
            pontos += 1
  
        pygameDisplay.update()
        clock.tick(60)

main()