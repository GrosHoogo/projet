import pygame
import sys
from pygame import mixer
import subprocess

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définition de la taille de l'écran
TAILLE_ECRAN = (1920, 1080)

# Création de la fenêtre en plein écran
fenetre = pygame.display.set_mode(TAILLE_ECRAN, pygame.FULLSCREEN)
pygame.display.set_caption("Interface avec Pygame")

# Musique de fond
mixer.music.load("background.mp3")
mixer.music.play(0)
mixer.music.set_volume(0.2)

# Application du background
image_fond = pygame.image.load("fond.jpg")
fond = pygame.transform.scale(image_fond, TAILLE_ECRAN)

# Importation de la bannière/logo
banner = pygame.image.load("quoquo.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x += 100
banner_rect.y = fenetre.get_height() // 2 - banner.get_height() // 2

# Création des boutons
largeur_bouton = 200
hauteur_bouton = 50
espacement_boutons = 10
pos_x_boutons = (TAILLE_ECRAN[0] - largeur_bouton) // 2
pos_y_bouton_jouer = (TAILLE_ECRAN[1] - (hauteur_bouton * 4 + espacement_boutons * 3)) // 2
bouton_jouer = pygame.Rect(pos_x_boutons, pos_y_bouton_jouer, largeur_bouton, hauteur_bouton)
bouton_regles = pygame.Rect(pos_x_boutons, pos_y_bouton_jouer + hauteur_bouton + espacement_boutons, largeur_bouton, hauteur_bouton)
bouton_quitter = pygame.Rect(pos_x_boutons, pos_y_bouton_jouer + (hauteur_bouton + espacement_boutons) * 3, largeur_bouton, hauteur_bouton)
bouton_retour = pygame.Rect(TAILLE_ECRAN[0] - 100, TAILLE_ECRAN[1] - 100, 80, 40)

# Booléens pour indiquer l'état des fenêtres
fenetre_regles_active = False
fenetre_principale_active = True

# Règles du jeu
texte_regles = """1- But du jeu :
Le but du jeu est d'être le premier joueur à atteindre le bord opposé du plateau avec son pion.

2- Matériel :
Le jeu Quoridor se joue sur un plateau de jeu composé de 81 cases carrées, disposées en 9x9.
Chaque joueur possède un pion de couleur distincte.
Les joueurs disposent également d'un certain nombre de barrières (généralement 10) pour bloquer le chemin de leur adversaire.

3- Déroulement du jeu :
Les joueurs jouent à tour de rôle, en commençant par le joueur qui possède les pions de couleur claire.
À chaque tour, un joueur peut effectuer l'une des deux actions suivantes :
a) Déplacer son pion : Le joueur peut déplacer son pion d'une case vers l'avant, vers l'arrière, vers la gauche ou vers la droite, mais pas en diagonale.
b) Placer une barrière : Le joueur peut placer une barrière sur le plateau pour bloquer le chemin de son adversaire. Les barrières doivent être placées de manière à ne pas bloquer complètement le plateau et à ne pas enfermer un joueur.

4- Règles des barrières :
Les barrières sont des blocs de deux cases de longueur et doivent être placées entre deux intersections du plateau.
Les barrières peuvent être placées verticalement ou horizontalement.
Les barrières ne peuvent pas être déplacées une fois qu'elles ont été placées.
Les joueurs peuvent sauter par-dessus les barrières avec leur pion.

5- Règles de mouvement :
Les pions peuvent se déplacer d'une case à la fois.
Les pions ne peuvent pas sauter par-dessus les barrières.
Les pions peuvent sauter par-dessus les pions adverses, mais pas les pions alliés.
Les pions ne peuvent pas revenir en arrière immédiatement lors de leur tour.

6- Conditions de victoire :
Le premier joueur à atteindre la rangée opposée du plateau avec son pion remporte la partie.
Si un joueur bloque complètement le passage de son adversaire avec des barrières de sorte qu'il ne puisse plus avancer, il remporte également la partie.
"""

# Fonction pour lancer la fenêtre de jeu
def lancer_jeu():
    subprocess.call(["python", "jeu.py"])  # Remplacez "jeu.py" par le nom de votre fichier de jeu

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Récupération des coordonnées du clic
            pos = pygame.mouse.get_pos()

            if fenetre_principale_active:
                # Vérification du clic sur les boutons dans la fenêtre principale
                if bouton_jouer.collidepoint(pos):
                    print("Bouton Jouer cliqué")
                    # Ajouter ici la fonctionnalité souhaitée pour le bouton "Jouer"
                    lancer_jeu()
                    fenetre_principale_active = False
                elif bouton_regles.collidepoint(pos):
                    print("Bouton Règles cliqué")
                    clic_son = mixer.Sound('clic.mp3')
                    clic_son.play()
                    mixer.music.stop()
                    # Activer la fenêtre "Règles"
                    fenetre_regles_active = True
                    fenetre_principale_active = False
                    regles_fenetre = pygame.display.set_mode(TAILLE_ECRAN, pygame.FULLSCREEN)
                    pygame.display.set_caption("Règles du jeu")
                    regles_fenetre.fill(BLANC)
                    # Faire disparaître l'image "banner"
                    banner_rect.x = TAILLE_ECRAN[0] + 100
                elif bouton_quitter.collidepoint(pos):
                    print("Bouton Quitter cliqué")
                    pygame.quit()
                    sys.exit()
            elif fenetre_regles_active:
                # Vérification du clic sur le bouton "Retour"
                if bouton_retour.collidepoint(pos):
                    print("Bouton Retour cliqué")
                    fenetre_principale_active = True
                    fenetre_regles_active = False

    # Affichage de l'image de fond et de la bannière
    fenetre.blit(fond, (0, 0))
    fenetre.blit(banner, banner_rect)

    if fenetre_principale_active:
        # Dessin des boutons dans la fenêtre principale
        pygame.draw.rect(fenetre, NOIR, bouton_jouer)
        pygame.draw.rect(fenetre, NOIR, bouton_regles)
        pygame.draw.rect(fenetre, NOIR, bouton_quitter)

        # Ajout du texte sur les boutons
        font = pygame.font.Font(None, 36)
        text_jouer = font.render("Jouer", True, BLANC)
        text_regles = font.render("Règles", True, BLANC)
        text_quitter = font.render("Quitter", True, BLANC)

        fenetre.blit(text_jouer,
                     (pos_x_boutons + largeur_bouton // 2 - text_jouer.get_width() // 2,
                      pos_y_bouton_jouer + hauteur_bouton // 2 - text_jouer.get_height() // 2))
        fenetre.blit(text_regles,
                     (pos_x_boutons + largeur_bouton // 2 - text_regles.get_width() // 2,
                      pos_y_bouton_jouer + (hauteur_bouton + espacement_boutons) * 1 + hauteur_bouton // 2 - text_regles.get_height() // 2))
        fenetre.blit(text_quitter,
                     (pos_x_boutons + largeur_bouton // 2 - text_quitter.get_width() // 2,
                      pos_y_bouton_jouer + (hauteur_bouton + espacement_boutons) * 3 + hauteur_bouton // 2 - text_quitter.get_height() // 2))

    elif fenetre_regles_active:
        # Affichage du texte des règles
        font_regles = pygame.font.Font(None, 36)
        texte_regles_sans_caracteres_speciaux = ''.join(c for c in texte_regles if c.isprintable())
        text_saisie_regles = font_regles.render(texte_regles_sans_caracteres_speciaux, True, NOIR)
        regles_fenetre.blit(text_saisie_regles, (50, 50))

        # Dessin du bouton "Retour"
        pygame.draw.rect(regles_fenetre, NOIR, bouton_retour)
        font_retour = pygame.font.Font(None, 24)
        text_retour = font_retour.render("Retour", True, BLANC)
        regles_fenetre.blit(text_retour, (TAILLE_ECRAN[0] - 80, TAILLE_ECRAN[1] - 80))

    # Rafraîchissement de l'affichage
    pygame.display.flip()
