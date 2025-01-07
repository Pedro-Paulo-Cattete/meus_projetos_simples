import pyautogui
import time

# Variáveis de configuração
intervalo = 0.08  # Intervalo entre cada pressionamento, em segundos

print("Pressione 'Ctrl+C' para parar o script.")

try:
    while True:
        pyautogui.press("space")  # Pressiona a tecla espaço
        time.sleep(intervalo)  # Aguarda o intervalo definido
except KeyboardInterrupt:
    print("\nScript parado pelo usuário.")