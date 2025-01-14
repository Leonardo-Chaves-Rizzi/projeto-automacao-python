import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 0.5 # pause de 0.8 segundos entre cada ação por padrão

# entrando no google
pg.click(x=52, y=886)
pg.write("chrome")
pg.press("enter")
pg.click(x=611, y=519)

time.sleep(1.5) # pause de 1 segundo

# pesquisando o sistema
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")

time.sleep(1.5) # pause de 1 segundo 

# fazendo o login no sistema
pg.click(x=574, y=376)
pg.write("testando@gmail.com")
pg.press("tab")
pg.write("senha123")
pg.press("tab")
pg.press("enter")

time.sleep(1.5) # pause de 1 segundo e meio

# cadastrando os produtos de "produtos.csv"
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    pg.click(x=570, y=256) # clicando no primeiro input

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pg.write(str(codigo))
    pg.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pg.write(str(marca))
    pg.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pg.write(str(tipo))
    pg.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pg.write(str(categoria))
    pg.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pg.write(str(preco_unitario))
    pg.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pg.write(str(custo))
    pg.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pg.write(obs)  
    pg.press("tab")

    pg.press("enter")
    pg.scroll(5000)