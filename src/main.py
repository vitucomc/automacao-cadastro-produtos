import pyautogui
import time
import pandas as pd
import os

# Pausa padrão entre os comandos do PyAutoGUI
pyautogui.PAUSE = 1


def abrir_navegador(link):
    """Abre o navegador Chrome e acessa o link informado"""
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(3)


def fazer_login(email, senha):
    """Realiza o login no sistema"""
    pyautogui.click(x=674, y=447)  # Campo de e-mail
    pyautogui.write(email)

    pyautogui.press("tab")
    pyautogui.write(senha)

    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(4)


def carregar_dados():
    """Carrega a base de dados CSV de forma portátil"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_csv = os.path.join(base_dir, "data", "produtos.csv")
    return pd.read_csv(caminho_csv)


def cadastrar_produto(produto):
    """Cadastra um único produto no sistema"""
    pyautogui.click(x=762, y=329)

    pyautogui.write(str(produto["codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["custo"]))
    pyautogui.press("tab")

    obs = str(produto["obs"])
    if obs.lower() != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    # Volta para o topo para cadastrar o próximo produto
    pyautogui.scroll(5000)


def main():
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    email = "pythonimpressionador@gmail.com"
    senha = "123456"

    abrir_navegador(link)
    fazer_login(email, senha)

    tabela = carregar_dados()

    for _, produto in tabela.iterrows():
        cadastrar_produto(produto)


if __name__ == "__main__":
    main()
