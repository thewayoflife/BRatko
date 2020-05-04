import pygame                   # import pygame - biblioteka za igrice
from pygame.locals import *     # kopira sva lokalna imena u pygame.locals

import pyaudio                  # import pyaudio - biblioteka za zvuk
import numpy as np              # import numpy - biblioteka za zvuk

# Zbog pyaudio i numpy predlažem korišćenje Anaconda3 umesto Python 3.7
# Python ima neki problem prilikom pip instalacije, ali sa Anacondom sve radi bez problema.

# Pokreni aplikaciju
pygame.init()

# Ubacivanje slike
img = pygame.image.load("radar1.png")

# Prozor aplikacije
screen = pygame.display.set_mode((927, 909))

# Petlja programa
done = False
while not done:
    # Proverava da li se bilo šta promenilo (tipa da li se miš pomerio)
    for event in pygame.event.get():
        
        # Uzima koordinate miša
        x, y = pygame.mouse.get_pos()
        
    # Ispisuje kordinate miša
    print("X: %d, Y: %d" %(x,y))

    # --------------------- Kreiranje zvuka --------------------
    p = pyaudio.PyAudio()

    volume = y/927   # Opseg [0.0, 1.0]
    fs = 44100       # Sampling rate, Hz, mora biti integer
    duration = 0.5   # U sekundama, može biti float
    f = x+441.0      # Sinusna frekvencija, Hz, može biti float

    # Generiše semplove, i radi konverziju u float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32) # sin(2𝛑ft)

    # Za paFloat32 sample vrednosti moraju biti u opsegu [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    # Pušta ton
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()
    # ----------------- Završeno kreiranje zvuka --------------------

    # Iscrtavanje elemenata u pygame prozoru
    pygame.display.set_caption("NMzSiAK") # Promeni ime prozora aplikacije
    screen.blit(img, (0,0)) # Iscrtavanje slike
    pygame.display.flip() # Update the full display Surface to the screen

    # Za gašenje aplikacije
    if event.type == pygame.QUIT:
        done = True

pygame.quit() 
