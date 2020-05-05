# Exercício Python #021 - Tocando um MP3

"""
DESAFIO 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

from time import sleep
from pygame import mixer

print('\n\033[1;31m3, 2, 1...')
sleep(3)
print('\n\033[7;36mMúsica iniciada.\033[m')
print('\n\033[1;34m 🔉 ⟲ ▶ ◼ ⏯  —————————— 2:26')
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('\nAperte enter para finalizar a música e o programa: ')

# O Pygame é uma biblioteca para fazer jogos, e tem uma funcionalidade para tocar sons, o mixer.
# É interessante aprender a usar algumas bibliotecas, mas não tentar aprender tudo, pois é tecnicamente
# impossível, e mesmo que fizesse isso a maioria das biblitoecas têm uso específico, por isso deve escolher bem
# quais irá aprender, para otimizar seu tempo em relação a isso.
# É bom ter esse leque de possibilidades para incrementar, ou resolver problemas.


# Usando outra biblioteca, a biblioteca playsound, de maneira mais simples:
'''
from playsound import _playsoundWin
_playsoundWin('ex021.mp3')
'''


# Código do vídeo (Não executou a música em minha máquina ao menos)
'''
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''
