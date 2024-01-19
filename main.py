import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 1

#abre o crome
pyautogui.press("win")
time.sleep(3)
pyautogui.write("crome")
time.sleep(5)
pyautogui.press("enter")
time.sleep(8)

#seleciona a conta
pyautogui.click(x=580, y=326)
time.sleep(4)

#abre uma nova guia
pyautogui.hotkey("ctrl", "t")
time.sleep(6)

#digita o link do site
pyautogui.click(x=556, y=58)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(8)

#faz login no site
pyautogui.click(x=638, y=376)
pyautogui.write("hirthhenryp@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234567890abcdefghij")
pyautogui.click(x=674, y=531)
time.sleep(5)

#cadastra todos os produtos
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=651, y=260)
    #codigo
    pyautogui.write(str(tabela.loc[linha , "codigo"]))
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha , "marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha , "tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha , "categoria"]))
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha , "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha , "custo"]))
    pyautogui.press("tab")
    #obs
    if not pd.isna(tabela.loc[linha , "obs"]):
        pyautogui.write(str(tabela.loc[linha , "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)