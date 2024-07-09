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

                elif changes_buttons_active and changes_button.collidepoint(event.pos):
                    print("Botão de alterações apertado")
                    # Implemente lógica para outra ação, se necessário

                elif current_screen == "servicos" and back_button.collidepoint(event.pos):
                    print("Botão de voltar apertado")
                    current_screen = "main"  # Volta para a tela principal
                    service_buttons_active = True
                    changes_buttons_active = True  # Reactiva os botões na tela principal

        screen.fill(WHITE)

        if current_screen == "main":
            draw_main_screen()
        elif current_screen == "servicos":
            draw_servicos_screen()

        pygame.display.flip()

def draw_main_screen():
    # Desenha a tela principal (tela de boas-vindas e botões)
    welcome_text = welcome_font.render("Bem Vindo!", True, BLACK)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_SIZE[0] // 2, 300))
    screen.blit(welcome_text, welcome_rect)
    
    draw_button(service_button, GRAY, "Serviços")
    draw_button(changes_button, GRAY, "Alterações")

def draw_servicos_screen():
    # Desenha a tela de serviços
    screen.fill(BLACK)  # Preenche a tela com preto para simular outra tela
    text = "Operação de Serviços"
    text_surface = button_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, 100))
    screen.blit(text_surface, text_rect)

    draw_button(back_button, GRAY, "Voltar")
    
    # Você pode adicionar outros elementos específicos da tela de serviços aqui

def draw_button(rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rectangle)

if __name__ == '__main__':
    
    button_width, button_height = 200, 50
    service_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 400, button_width, button_height))
    changes_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 500, button_width, button_height))
    back_button = pygame.Rect((20, 20, 100, 50))  # Exemplo de posição e tamanho do botão de voltar
    
    main()
