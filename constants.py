import pygame

# Constants
width, height = 800, 800
rows, cols = 8, 8
square_size = width // cols

# RGB
White = (242, 242, 242)
Black = (0, 0, 0)
lsquare = (232, 235, 239)
dsquare = (125, 135, 150)
gray = (128,128,128)
Blue = (0, 0, 255)
crown = pygame.transform.scale(pygame.image.load('crown.png'), (45, 25))