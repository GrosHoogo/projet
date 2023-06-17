import pygame
import subprocess

# Initialise pygame
pygame.init()

# Initialise la fenetre pygame
TAILLE_ECRAN = (1920, 1080)
fenetre = pygame.display.set_mode(TAILLE_ECRAN)
pygame.display.set_caption("Choisissez la taille du plateau, le nombre de joueurs et le nombre de barrières")

# Défini les différentes tailles de plateau de jeu, le nombre de joueurs et le nombre de barrières
board_sizes = ["5x5", "7x7", "9x9", "11x11"]
num_players = ["2", "4"]
num_barriers = list(range(4, 41, 4))  # Select multiples of 4 from 4 to 40

# Configure la police d'écriture
font = pygame.font.SysFont(None, 30)

# Crée un text object pour chaque taille de plateau de jeu, le nombre de joueurs et le nombre de barrières
board_text_objects = [font.render(size, True, (255, 255, 255)) for size in board_sizes]
players_text_objects = [font.render(player, True, (255, 255, 255)) for player in num_players]
barriers_text_objects = [font.render(str(barrier), True, (255, 255, 255)) for barrier in num_barriers]

# Calcule la position de chaque text sur la fenetre
board_text_positions = [(TAILLE_ECRAN[0]//4 - text.get_width()//2, TAILLE_ECRAN[1]//2 - text.get_height()//2 + 100*i - 60) for i, text in enumerate(board_text_objects)]
players_text_positions = [(3*TAILLE_ECRAN[0]//4 - text.get_width()//2, TAILLE_ECRAN[1]//2 - text.get_height()//2 + 100*i - 60) for i, text in enumerate(players_text_objects)]
barriers_text_positions = [(TAILLE_ECRAN[0]//2 - text.get_width()//2, TAILLE_ECRAN[1]//2 - text.get_height()//2 + 50*i - 60) for i, text in enumerate(barriers_text_objects)]

# Calcule la position de chaque rectangle sur la fenetre
board_rect_positions = [(pos[0] - 10, pos[1] - 10, text.get_width() + 20, text.get_height() + 20) for pos, text in zip(board_text_positions, board_text_objects)]
players_rect_positions = [(pos[0] - 10, pos[1] - 10, text.get_width() + 20, text.get_height() + 20) for pos, text in zip(players_text_positions, players_text_objects)]
barriers_rect_positions = [(pos[0] - 10, pos[1] - 10, text.get_width() + 20, text.get_height() + 20) for pos, text in zip(barriers_text_positions, barriers_text_objects)]

# Crée un bouton de validation
validation_text = font.render("Valider", True, (255, 255, 255))
validation_position = (TAILLE_ECRAN[0]//2 - validation_text.get_width()//2, TAILLE_ECRAN[1] - 100)
validation_rect_position = (validation_position[0] - 10, validation_position[1] - 10, validation_text.get_width() + 20, validation_text.get_height() + 20)

# Indices des sélections
selected_board_size_index = None
selected_num_players_index = None
selected_num_barriers_index = None

# Boucle pygame
clock = pygame.time.Clock()

# Ouvre la fenêtre de selection
running = True
while running:
    # events pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # prends la position du curseur de la souris
            x, y = pygame.mouse.get_pos()

            # Check si le click est sur un texte correspondant à la taille du plateau de jeu
            for i, pos in enumerate(board_rect_positions):
                if pos[0] <= x <= pos[0] + pos[2] and pos[1] <= y <= pos[1] + pos[3]:
                    # met à jour la sélection
                    selected_board_size_index = i

            # Check si le click est sur un texte correspondant au nombre de joueurs
            for i, pos in enumerate(players_rect_positions):
                if pos[0] <= x <= pos[0] + pos[2] and pos[1] <= y <= pos[1] + pos[3]:
                    # met à jour la sélection
                    selected_num_players_index = i

            # Check si le click est sur un texte correspondant au nombre de barrières
            for i, pos in enumerate(barriers_rect_positions):
                if pos[0] <= x <= pos[0] + pos[2] and pos[1] <= y <= pos[1] + pos[3]:
                    # met à jour la sélection
                    selected_num_barriers_index = i

            # Vérifie si le bouton de validation a été cliqué
            if validation_rect_position[0] <= x <= validation_rect_position[0] + validation_rect_position[2] and validation_rect_position[1] <= y <= validation_rect_position[1] + validation_rect_position[3]:
                if selected_board_size_index is not None and selected_num_players_index is not None and selected_num_barriers_index is not None:
                    # Exécute le fichier "game.py" avec les paramètres choisis comme arguments et ferme la fenêtre
                    subprocess.call(["python", "game.py", board_sizes[selected_board_size_index], num_players[selected_num_players_index], str(num_barriers[selected_num_barriers_index])])
                    running = False

    # Nettoie la fenêtre pygame
    fenetre.fill((0, 0, 0))

    # Affiche les rectangles autour des text objects
    for i, rect in enumerate(board_rect_positions):
        if i == selected_board_size_index:
            pygame.draw.rect(fenetre, (255, 255, 255), rect)  # rectangle rempli pour la sélection
            selected_text = font.render(board_sizes[i], True, (0, 0, 0))  # texte en noir pour la sélection
            fenetre.blit(selected_text, board_text_positions[i])
        else:
            pygame.draw.rect(fenetre, (255, 255, 255), rect, 2)  # rectangle non rempli pour les non-sélections
            fenetre.blit(board_text_objects[i], board_text_positions[i])  # texte en blanc pour les non-sélections

    for i, rect in enumerate(players_rect_positions):
        if i == selected_num_players_index:
            pygame.draw.rect(fenetre, (255, 255, 255), rect)  # rectangle rempli pour la sélection
            selected_text = font.render(num_players[i], True, (0, 0, 0))  # texte en noir pour la sélection
            fenetre.blit(selected_text, players_text_positions[i])
        else:
            pygame.draw.rect(fenetre, (255, 255, 255), rect, 2)  # rectangle non rempli pour les non-sélections
            fenetre.blit(players_text_objects[i], players_text_positions[i])  # texte en blanc pour les non-sélections

    for i, rect in enumerate(barriers_rect_positions):
        if i == selected_num_barriers_index:
            pygame.draw.rect(fenetre, (255, 255, 255), rect)  # rectangle rempli pour la sélection
            selected_text = font.render(str(num_barriers[i]), True, (0, 0, 0))  # texte en noir pour la sélection
            fenetre.blit(selected_text, barriers_text_positions[i])
        else:
            pygame.draw.rect(fenetre, (255, 255, 255), rect, 2)  # rectangle non rempli pour les non-sélections
            fenetre.blit(barriers_text_objects[i], barriers_text_positions[i])  # texte en blanc pour les non-sélections

    # Affiche le rectangle autour du bouton de validation
    pygame.draw.rect(fenetre, (255, 255, 255), validation_rect_position, 2)

    # Affiche le bouton de validation
    fenetre.blit(validation_text, validation_position)

    # Update la fenêtre pygame
    pygame.display.update()

# Quitte la fenêtre pygame
pygame.quit()


