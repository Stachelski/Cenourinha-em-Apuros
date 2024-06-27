import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("recursos/iconedog.png")

dog = pygame.image.load("recursos/dog.png")
fundo = pygame.image.load("recursos/fundo.jpg")
fundoStart = pygame.image.load("recursos/fundoStart.png")
fundoDead = pygame.image.load("recursos/fundoDead.png")

chinelo = pygame.image.load("recursos/chinelo.png")
jornal = pygame.image.load("recursos/jornal.png")
osso = pygame.image.load("recursos/osso.png")
tamanho = (735,591)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Jogo do cachorrinho")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("recursos/missile.wav")
explosaoSound = pygame.mixer.Sound("recursos/explosao.wav")
fonte = pygame.font.SysFont("impact",28)
fonteStart = pygame.font.SysFont("impact",54)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("recursos/ironsound.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )
laranja = (209,154,41)
verde = (88,158,73)
amarelo = (255,255,0)

def jogar(nome):
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 400
    movimentoXPersona  = 0
    #movimentoYPersona  = 0
    posicaoXchinelo = 400
    posicaoYchinelo = -240
    velocidadeChinelo = 1
    posicaoXjornal = 200
    posicaoYjornal = -240
    velocidadeJornal = 2
    pontos = 0
    larguraPersona = 101
    alturaPersona = 179
    larguraChinelo  = 31
    alturaChinelo  = 66
    larguraJornal  = 38
    alturaJornal  = 50
    dificuldade  = 20

    posXosso = 0
    posYosso = 455
    vel = 3

    sol = 50
    crescimento = 0.1
    maxCrescimento = 3
    posSol = (60,110)
    direcaoCrescimento = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
            #elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            #    movimentoYPersona = -10
            #elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            #    movimentoYPersona = 10
            #elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            #    movimentoYPersona = 0
            #elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            #    movimentoYPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        #posicaoYPersona = posicaoYPersona + movimentoYPersona
                    
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona > 630:
            posicaoXPersona = 620
            
        if posicaoYPersona < 0 :
            posicaoYPersona = 10
        elif posicaoYPersona > 473:
            posicaoYPersona = 463
        
        posXosso += vel
        if posXosso > tamanho [0]:
            posXosso = -200
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( osso, (posXosso, posYosso))
        tela.blit( dog, (posicaoXPersona, posicaoYPersona) )
        
        posicaoYchinelo = posicaoYchinelo + velocidadeChinelo
        if posicaoYchinelo > 600:
            posicaoYchinelo = -240
            pontos = pontos + 1
            velocidadeChinelo = velocidadeChinelo + 1
            posicaoXchinelo = random.randint(0,800)
            #pygame.mixer.Sound.play(missileSound)
            
        posicaoYjornal = posicaoYjornal + velocidadeJornal
        if posicaoYjornal > 600:
            posicaoYjornal = -240
            pontos = pontos + 1
            velocidadeJornal = velocidadeJornal + 1
            posicaoXjornal = random.randint(0,800)
            
        tela.blit( chinelo, (posicaoXchinelo, posicaoYchinelo) )
        tela.blit( jornal, (posicaoXjornal, posicaoYjornal) )

        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, laranja)
        tela.blit(texto, (10,10))
        
        pygame.draw.circle(tela,amarelo,posSol,int(sol))
        sol += crescimento * direcaoCrescimento
        if sol >= 50 + maxCrescimento or sol <= 50 - maxCrescimento:
            direcaoCrescimento *= -1

        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsChineloX = list(range(posicaoXchinelo, posicaoXchinelo + larguraChinelo))
        pixelsChineloY = list(range(posicaoYchinelo, posicaoYchinelo + alturaChinelo))
        pixelsJornalX = list(range(posicaoXjornal, posicaoXjornal + larguraJornal))
        pixelsJornalY = list(range(posicaoYjornal, posicaoYjornal + alturaJornal))

        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsChineloY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsChineloX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        if  len( list( set(pixelsJornalY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsJornalX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
    
        
        pygame.display.update()
        relogio.tick(60)


def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, laranja, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,500))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,500))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Jogo do cachorrinho","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, branco, (420,460,170,100),0,30)
        buttonStart = pygame.draw.rect(tela, laranja, (425,465,160,90),0,25)
        buttonRanking = pygame.draw.rect(tela, laranja, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,55))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (440,475))

        
        
        pygame.display.update()
        relogio.tick(60)

start()