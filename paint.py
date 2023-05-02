import time
import pyautogui

# Passo 1 -> Abrir o Paint

pyautogui.hotkey('win', 'r')
pyautogui.press('backspace')
time.sleep(5)
pyautogui.write('mspaint')
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)

# Passo 2 -> Desenhar

pyautogui.moveTo(571, 250)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up


# Passo 3 -> Salvar

time.sleep(7)
pyautogui.click(1339,0)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('backspace')
time.sleep(3)
pyautogui.write('Hello_World')
time.sleep(3)
pyautogui.press('enter')
