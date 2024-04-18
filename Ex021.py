#Faça um programa em Python que abra e reproduza o áudio de um arquivo em MP3

import pygame

#pygame é uma das bibliotecas mais famosas de jogos em Python
#para iniciá-la é necessário o comando pygame.init()

pygame.init()

#pygame possui funcionalidades para criar jogos
#ele possui funções para carregar imagens, sons, vídeos, etc...

#Para este exercício será utilizada a funcionalidade mixer(áudio) do pygame

pygame.mixer.music.load('maisumvoo.mp3')
#Vai upar(carregar) o arquivo de áudio

pygame.mixer.music.play() #Vai dar play no áudio

pygame.event.wait() #Vai esperar o evento 'pygame.mixer.music.play()' ser executado para que o programa finalize a execução


