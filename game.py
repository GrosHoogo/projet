import pygame
import sys

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Set the default board size
default_board_size = 8

# Get board size from command line arguments or use the default size
if len(sys.argv) > 1:
    board_size_str = sys.argv[1]
    board_size = int(board_size_str.split("x")[0])
else:
    board_size = default_board_size

# Rest of the code...

# Define the size of each cell in pixels
cell_size = 60

# Calculate the size of the window based on the board size and cell size
window_size = (board_size * cell_size + (board_size + 1) * 2, board_size * cell_size + (board_size + 1) * 2)

# Initialize the window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Board")

# Set the font for the text
font = pygame.font.SysFont(None, 30)

# Draw the board
def draw_board():
    # Clear the window
    window.fill(BLACK)

    # Draw the cells
    for i in range(board_size):
        for j in range(board_size):
            # Calculate the position of the cell
            cell_x = j * cell_size + (j+1) * 2
            cell_y = i * cell_size + (i+1) * 2

            # Draw the cell
            pygame.draw.rect(window, GRAY, (cell_x, cell_y, cell_size, cell_size))

    # Draw the vertical lines
    for i in range(board_size+1):
        line_x = i * (cell_size + 2)
        pygame.draw.line(window, BLACK, (line_x, 2), (line_x, window_size[1]-2), 2)

    # Draw the horizontal lines
    for i in range(board_size+1):
        line_y = i * (cell_size + 2)
        pygame.draw.line(window, BLACK, (2, line_y), (window_size[0]-2, line_y), 2)


# Draw the board initially
draw_board()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the window
    pygame.display.update()

# Quit pygame
pygame.quit()
