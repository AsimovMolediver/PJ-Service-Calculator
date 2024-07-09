import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Variáveis das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Tamanho da janela
WINDOW_SIZE = (800, 600)

# Criação da janela com os parâmetros informados e nome da janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('C.D.S.A')

# Fontes utilizadas no programa
button_font = pygame.font.Font(None, 32)
welcome_font = pygame.font.Font(None, 48)

def main():

    # Variáveis para as janelas/telas
    current_screen = "main"  # Indica a tela atual, inicialmente a tela principal
    service_buttons_active = True  # Botões "Serviços" estão ativos inicialmente
    changes_buttons_active = True  # Botões "Alterações" estão ativos inicialmente
    result_button_active = False

    # Variáveis para os campos de entrada
    input1 = ''
    input2 = ''
    active_input1 = False
    active_input2 = False
    result = None

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if service_buttons_active and service_button.collidepoint(event.pos):
                    print("Botão de serviço apertado")
                    current_screen = "servicos"  # Altera para a tela de serviços
                    service_buttons_active = False
                    changes_buttons_active = False
                    result_button_active = True

                elif changes_buttons_active and changes_button.collidepoint(event.pos):
                    print("Botão de alterações apertado")
                    # Implemente lógica para outra ação, se necessário

                elif current_screen == "servicos":
                    if back_button.collidepoint(event.pos):
                        print("Botão de voltar apertado")
                        current_screen = "main"  # Volta para a tela principal
                        service_buttons_active = True
                        changes_buttons_active = True  # Reactiva os botões na tela principal
                        input1 = ''
                        input2 = ''
                        result = None
                    elif input1_box.collidepoint(event.pos):
                        active_input1 = True
                        active_input2 = False
                    elif input2_box.collidepoint(event.pos):
                        active_input1 = False
                        active_input2 = True
                    elif result_button_active and result_button.collidepoint(event.pos) and input1 and input2:
                        try:
                            num1 = float(input1)
                            num2 = float(input2)
                            result = num1 + num2
                        except ValueError:
                            result = "Erro: Entrada inválida"
                    else:
                        active_input1 = False
                        active_input2 = False

            elif event.type == pygame.KEYDOWN:
                if current_screen == "servicos":
                    if active_input1:
                        if event.key == pygame.K_RETURN:
                            active_input1 = False
                        elif event.key == pygame.K_BACKSPACE:
                            input1 = input1[:-1]
                        else:
                            input1 += event.unicode
                    elif active_input2:
                        if event.key == pygame.K_RETURN:
                            active_input2 = False
                        elif event.key == pygame.K_BACKSPACE:
                            input2 = input2[:-1]
                        else:
                            input2 += event.unicode

        screen.fill(WHITE)

        if current_screen == "main":
            draw_main_screen()
        elif current_screen == "servicos":
            draw_servicos_screen(input1, input2, result, active_input1, active_input2)

        pygame.display.flip()

def draw_main_screen():
    # Desenha a tela principal (tela de boas-vindas e botões)
    welcome_text = welcome_font.render("Bem Vindo!", True, BLACK)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_SIZE[0] // 2, 300))
    screen.blit(welcome_text, welcome_rect)
    
    draw_button(service_button, GRAY, "Serviços")
    draw_button(changes_button, GRAY, "Alterações")

def draw_servicos_screen(input1, input2, result, active_input1, active_input2):
    # Desenha a tela de serviços
    screen.fill(WHITE)  # Preenche a tela com branco
    text = "Operação de Serviços"
    text_surface = button_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, 100))
    screen.blit(text_surface, text_rect)

    draw_button(back_button, GRAY, "Voltar")
    draw_button(result_button, GRAY, "Resultado")

    # Desenha os campos de entrada
    draw_input_box(input1_box, input1, active_input1)
    draw_input_box(input2_box, input2, active_input2)

    # Exibe o resultado se houver
    if result is not None:
        result_text = f"Resultado: {result}"
        result_surface = button_font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(center=(WINDOW_SIZE[0] // 2, 375))
        screen.blit(result_surface, result_rect)
    
def draw_button(rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rectangle)

def draw_input_box(rect, text, active):
    color = RED if active else GRAY
    pygame.draw.rect(screen, color, rect, 2)
    text_surface = button_font.render(text, True, BLACK)
    screen.blit(text_surface, (rect.x + 5, rect.y + 5))

if __name__ == '__main__':
    
    button_width, button_height = 200, 50
    service_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 400, button_width, button_height))
    changes_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 500, button_width, button_height))
    back_button = pygame.Rect((20, 20, 100, 50))  # Exemplo de posição e tamanho do botão de voltar
    
    input_box_width, input_box_height = 200, 50
    input1_box = pygame.Rect((WINDOW_SIZE[0] // 2 - input_box_width // 2, 200, input_box_width, input_box_height))
    input2_box = pygame.Rect((WINDOW_SIZE[0] // 2 - input_box_width // 2, 300, input_box_width, input_box_height))

    result_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 400, button_width, button_height))
    
    main()
