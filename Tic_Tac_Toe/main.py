import pygame as py
import sys
import numpy as np

# Initialize Pygame
py.init()

# Define colors
white = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)
green = (0, 255, 0)
bg_color = (28, 170, 156)
black = (0, 0, 0)

# Define dimensions
width = 450
height = 450
line_width = 5
rows = columns = 3
square_size = width // columns
circle_radius = square_size // 3
circle_width = 15
cross_width = 25

# Set up the display
screen = py.display.set_mode((width, height + 150))
py.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

# Create a board
board = np.zeros((rows, columns))


# Function to draw grid lines
def draw_lines(color=white):
    for i in range(1, 4):
        py.draw.line(screen, color, (0, square_size * i), (width, square_size * i), line_width)
    for i in range(1, columns):
        py.draw.line(screen, color, (square_size * i, 0), (square_size * i, height), line_width)


# Function to draw X and O figures
def draw_figures(color=white):
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 1:
                py.draw.circle(screen, color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)
            elif board[row][col] == 2:
                py.draw.line(screen, color, (col * square_size + square_size // 4, row * square_size + square_size // 4),
                             (col * square_size + 3 * square_size // 4, row * square_size + 3 * square_size // 4), cross_width)
                py.draw.line(screen, color,
                             (col * square_size + square_size // 4, row * square_size + 3 * square_size // 4),
                             (col * square_size + 3 * square_size // 4, row * square_size + square_size // 4), cross_width)


# Function to mark a square with a player's move
def mark_square(row, col, player):
    board[row][col] = player


# Function to check if a square is available
def available_square(row, col):
    return board[row][col] == 0


# Function to check if the board is full
def is_board_full(check_board=board):
    for row in range(rows):
        for col in range(columns):
            if check_board[row][col] == 0:
                return False
    return True


# Function to check if a player has won
def check_winner(player, check_board=board):
    for col in range(columns):
        if all(check_board[row][col] == player for row in range(rows)):
            return True

    for row in range(rows):
        if all(check_board[row][col] == player for col in range(columns)):
            return True

    if all(check_board[i][i] == player for i in range(min(rows, columns))):
        return True

    if all(check_board[i][columns - 1 - i] == player for i in range(min(rows, columns))):
        return True

    return False


# Minimax algorithm to determine the best move for the AI
def minimax(minimax_board, depth, is_maximizing):
    if check_winner(2, minimax_board):
        return float('inf')
    elif check_winner(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(rows):
            for col in range(columns):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(rows):
            for col in range(columns):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


# Function to find the best move for the AI
def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False


# Function to restart the game
def restart_game():
    screen.fill(bg_color)
    draw_lines()
    restart_button.draw()
    for row in range(rows):
        for col in range(columns):
            board[row][col] = 0


# Set up font for text display
text_font = py.font.SysFont(None, 110, italic=True, bold=True)


# Function to draw text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Load button image
restart_img = py.image.load("restart.png").convert_alpha()


# Button class for the restart button
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = py.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # Get mouse position
        pos = py.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if py.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# Initialize the restart button
restart_button = Button(100, 490, restart_img, 0.4)

# Draw initial lines on the screen
draw_lines()
restart_button.draw()

# Initialize game variables
player = 1
game_over = False

# Main game loop
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

        if event.type == py.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // square_size
            mouseY = event.pos[1] // square_size

            if mouseY < rows and available_square(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_winner(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_winner(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if is_board_full():
                        game_over = True

        if event.type == py.MOUSEBUTTONDOWN:
            if restart_button.draw():
                restart_game()
                game_over = False
                player = 1

    if not game_over:
        draw_figures()
    else:
        if check_winner(1):
            draw_figures(green)
            draw_lines(green)
        elif check_winner(2):
            draw_lines(red)
            draw_figures(red)
            draw_text('You Lost ', text_font, white, 60, 180)
        else:
            draw_lines(gray)
            draw_figures(gray)
            draw_text('Tie ', text_font, white, 170, 180)

    py.display.update()
