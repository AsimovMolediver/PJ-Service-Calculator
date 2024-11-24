import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Variáveis das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 244, 196)
BLUE = (0, 0, 255)


# Tamanho da janela
WINDOW_SIZE = (400, 600)

# Criação da janela com os parâmetros informados e nome da janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('C.D.S - Calculadora de Serviços')

# Fontes utilizadas no programa (Courier)
button_font = pygame.font.SysFont('Courier', 18)
button_fontav = pygame.font.SysFont('Courier', 15)
button_fontent = pygame.font.SysFont('Courier', 29)
welcome_font = pygame.font.SysFont('Courier', 32)

# Formatação para o dinheiro ser printado como real e só ter duas casas decimais
def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():

    # Variáveis para as janelas/telas
    current_screen = "main"  # Indica a tela atual, inicialmente a tela principal
    service_buttons_active = True  # Botões "Serviços" estão ativos inicialmente
    result_button_active = False

    # Variáveis para os campos de entrada
    num1 = ''
    active_num1 = False
    result_l = None
    result_iss = None
    result_inss = None
    result_irpf = None

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if service_buttons_active and service_button.collidepoint(event.pos):
                    ##print("Botão de serviço apertado")
                    current_screen = "servicos"  # Altera para a tela de serviços
                    service_buttons_active = False
                    result_button_active = True

                elif current_screen == "servicos":

                    if back_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                    elif num1_box.collidepoint(event.pos):
                        active_num1 = True

                    elif result_button_active and result_button.collidepoint(event.pos) and num1:
                        try:
                            num1 = float(num1)
                            result_iss = num1 * 0.05
                            result_inss = num1 * 0.11

                            if num1 < 2259.21:
                                result_irpf = 00.00
                            elif num1 > 2259.21 and num1 <= 2826.65:
                                result_irpf = (num1 * 0.075) - 169.44
                            elif num1 >= 2826.66 and num1 <= 3751.05:
                                result_irpf = (num1 * 0.15) - 381.44
                            elif num1 >= 3751.06 and num1 <= 4664.68:
                                result_irpf = (num1 * 0.225) - 662.77
                            elif num1 > 4664.68:
                                result_irpf = (num1 * 0.275) - 899.00

                            result_l = num1 - (result_iss + result_inss + result_irpf)
                            num1 = str(num1)  # Convertendo de volta para string
                            ##print(result_l, result_iss, result_inss, result_irpf)
                            
                        except ValueError:
                            result_l = "Erro: Entrada inválida"
                    else:
                        active_num1 = False

                    # Botão Limpar: resetar todos os campos
                    if clear_button.collidepoint(event.pos):
                        num1 = ''
                        result_l = None
                        result_iss = None
                        result_inss = None
                        result_irpf = None
                        active_num1 = False

            elif event.type == pygame.KEYDOWN:
                if current_screen == "servicos":
                    if active_num1:
                        if event.key == pygame.K_RETURN:
                            active_num1 = False
                        elif event.key == pygame.K_BACKSPACE:
                            num1 = num1[:-1]
                        else:
                            num1 += event.unicode

        screen.fill(WHITE)

        if current_screen == "main":
            draw_main_screen()
        elif current_screen == "servicos":
            draw_servicos_screen(num1, result_l, result_inss, result_iss, result_irpf, active_num1)

        pygame.display.flip()

def draw_main_screen():
    # Desenha a tela principal (tela de boas-vindas e botões)
    screen.fill(YELLOW)
    welcome_text = welcome_font.render("Bem Vindo!", True, BLACK)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_SIZE[0] // 2, 300))
    screen.blit(welcome_text, welcome_rect)
    
    draw_button(service_button, GRAY, "Serviço CPF")

def draw_servicos_screen(num1, result_l, result_inss, result_iss, result_irpf, active_num1):
    # Desenha a tela de serviços
    screen.fill(YELLOW)  # Preenche a tela com Amarelo
    text = "Operação de Serviço"
    text_surface = button_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, 100))
    screen.blit(text_surface, text_rect)

    texta = "R$:"
    text_surface = button_fontent.render(texta, True, BLACK)
    text_rect = text_surface.get_rect(left=40, top=207)
    screen.blit(text_surface, text_rect)

    textb = "Utilize o ponto '.' para os centavos."
    text_surface = button_fontav.render(textb, True, BLACK)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, 165))
    screen.blit(text_surface, text_rect)

    draw_buttonB(back_button, RED, "Sair")
    draw_button(result_button, GRAY, "Resultado")
    draw_button(clear_button, GRAY, "Limpar")

    # Desenha os campos de entrada
    draw_input_box(num1_box, num1, active_num1)

    # Exibe o resultado se houver
    if result_l is not None:
        result_text = f"Resultado Líquido: {format_currency(result_l)}"
        result_surface = button_font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(left=20, top=550)  # Posição ajustada para a caixa de resultado líquido
        screen.blit(result_surface, result_rect)
    
    if result_iss is not None:
        result_text = f"ISS: {format_currency(result_iss)}"
        result_surface = button_font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(left=20, top=525)  # Ajuste da posição
        screen.blit(result_surface, result_rect)

    if result_inss is not None:
        result_text = f"INSS: {format_currency(result_inss)}"
        result_surface = button_font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(left=20, top=500)  # Ajuste da posição
        screen.blit(result_surface, result_rect)
    
    if result_irpf is not None:
        result_text = f"IRPF: {format_currency(result_irpf)}"
        result_surface = button_font.render(result_text, True, BLACK)
        result_rect = result_surface.get_rect(left=20, top=475)  # Ajuste da posição
        screen.blit(result_surface, result_rect)

def draw_buttonB(rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, WHITE)
    text_rectangle = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rectangle)

def draw_button(rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, BLACK)
    text_rectangle = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rectangle)

def draw_input_box(rect, text, active):
    color = BLUE if active else GRAY
    pygame.draw.rect(screen, color, rect, 2)
    text_surface = button_font.render(str(text), True, BLACK)  # Convertendo text para string
    screen.blit(text_surface, (rect.x + 5, rect.y + 5))

if __name__ == '__main__':
    
    button_width, button_height = 200, 50
    service_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 400, button_width, button_height))
    back_button = pygame.Rect((320, 0, 80, 40))  #Posição e tamanho do botão de voltar
    clear_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 300, button_width, button_height))  # Posição do botão Limpar
    
    input_box_width, input_box_height = 200, 50
    num1_box = pygame.Rect((WINDOW_SIZE[0] // 2 - input_box_width // 2, 200, input_box_width, input_box_height))

    result_button = pygame.Rect((WINDOW_SIZE[0] // 2 - button_width // 2, 400, button_width, button_height))
    
    main()
