import pygame
import sys

# inicializa Pygame
pygame.init()

# define as dimensões da tela
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# define as cores
white = (255, 255, 255)
black = (0, 0, 0)

# matriz para armazenar o estado do jogo
board = [[None for _ in range(3)] for _ in range(3)]

# função pra desenhar o tabuleiro
def draw_board():
    screen.fill(white)
    for i in range(1, 3):
        pygame.draw.line(screen, black, (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, black, (i * 200, 0), (i * 200, 600), 5)

# função pra desenhar um X ou O na tela
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 120)
    text = font.render(symbol, 1, black)
    screen.blit(text, (col * 200 + 80, row * 200 + 80))

# função pra verificar se alguém ganhou
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# loop principal
current_symbol = "X"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # obter posição do clique
            pos = pygame.mouse.get_pos()
            # converte a posição pra coordenadas do tabuleiro
            row, col = pos[1] // 200, pos[0] // 200
            # verifica se a posição é válida
            if board[row][col] is None:
                board[row][col] = current_symbol
                # verifica se alguém ganhou
                winner = check_win()
                if winner is not None:
                    print(f"O jogador {winner} ganhou!")
                    pygame.quit()
                    sys.exit()
                # alterna o símbolo
                current_symbol = "O" if current_symbol == "X" else "X"

    # desenha o tabuleiro e os símbolos
    draw_board()
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                draw_symbol(i, j, board[i][j])
    pygame.display.flip()
    