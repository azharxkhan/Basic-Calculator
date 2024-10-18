import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Calculator")

font = pygame.font.SysFont('Arial', 32)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', 'C'],
    ['+', '0', '-', '=']
]

def draw_buttons():
    button_width = WIDTH // 4
    button_height = HEIGHT // 6
    for row_idx, row in enumerate(buttons):
        for col_idx, button in enumerate(row):
            x = col_idx * button_width
            y = row_idx * button_height + 200
            pygame.draw.rect(screen, GRAY, (x, y, button_width, button_height), 2)
            text_surface = font.render(button, True, BLACK)
            screen.blit(text_surface, (x + button_width // 2 - text_surface.get_width() // 2, y + button_height // 2 - text_surface.get_height() // 2))

def draw_display(current_input):
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 100))
    text_surface = font.render(current_input, True, BLACK)
    screen.blit(text_surface, (10, 50 - text_surface.get_height() // 2))

def run_basic_calculator():
    current_input = ""
    running = True
    while running:
        screen.fill(WHITE)
        draw_buttons()
        draw_display(current_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y > 200:
                    row = (y - 200) // (HEIGHT // 6)
                    col = x // (WIDTH // 4)
                    button_value = buttons[row][col]

                    if button_value == 'C':
                        current_input = ""
                    elif button_value == '=':
                        try:
                            current_input = str(eval(current_input))
                        except:
                            current_input = "Error"
                    else:
                        current_input += button_value

        pygame.display.update()

    pygame.quit()
    sys.exit()

run_basic_calculator()
