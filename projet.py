import pygame
import sys


# Définit la taille de la grille (carrée)
grid_size = 10

# Définit le nombre de joueurs
num_players = 2

# Définit la taille de l'écran
screen_width = 800
screen_height = 600

# Initialise Pygame
pygame.init()

# Initialise la fenêtre d'affichage
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("QuoridorTest")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Taille d'une case de la grille
cell_size = min(screen_width // grid_size, screen_height // grid_size)

# Position des pions pour chaque joueur
player_positions = {}
for i in range(num_players):
    if i % 2 == 0:
        player_positions[i] = (0, i * (grid_size-1))
    else:
        player_positions[i] = ((grid_size-1)*cell_size, (i-1)*(grid_size-1))

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Efface l'écran
    screen.fill(white)

    # Dessine la grille
    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, black, rect, 1)

    # Dessine les pions
    for player, position in player_positions.items():
        pygame.draw.circle(screen, blue, position, cell_size // 2)

    # Met à jour l'affichage
    pygame.display.update()
