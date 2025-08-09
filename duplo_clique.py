import pyautogui
import keyboard
import time

# Opcional: Pausa entre as ações do pyautogui
# pyautogui.PAUSE = 0.5 

# Variável de controle para o estado do duplo clique
double_click_enabled = False

def toggle_double_click():
    """Função para alternar o estado de ativação do duplo clique."""
    global double_click_enabled
    double_click_enabled = not double_click_enabled
    if double_click_enabled:
        print("Duplo clique ATIVADO. Mova o mouse para a posição desejada.")
    else:
        print("Duplo clique DESATIVADO.")

# Registra a tecla 'p' para chamar a função toggle_double_click
keyboard.add_hotkey('p', toggle_double_click)

print("Pressione 'P' para ATIVAR/DESATIVAR o duplo clique.")
print("Pressione 'Esc' para SAIR do programa a qualquer momento.")

try:
    while True:
        if double_click_enabled:
            # Pressiona o botão esquerdo do mouse duas vezes rapidamente
            pyautogui.doubleClick()
            # Adicione um pequeno atraso para evitar cliques excessivos ou descontrolados
            time.sleep(0.5) # Ajuste este valor se precisar de cliques mais rápidos ou lentos
        
        # Permite que o programa seja interrompido pela tecla 'Esc'
        if keyboard.is_pressed('esc'):
            print("Saindo do programa.")
            break
        
        time.sleep(0.01) # Pequeno delay para não consumir 100% da CPU
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")
finally:
    keyboard.unhook_all() # Garante que todos os hooks do teclado sejam liberados ao sair