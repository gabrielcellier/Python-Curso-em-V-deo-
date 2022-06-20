#faça um programa que abra e reproduza um audio de arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('pth.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass

#correção mudou desde que o curso foi criado.