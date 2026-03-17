import json
from logica import logicafacil,logicadificil,logicamedia
algo=True




def menu(x):
    print("----------------------------")
    print(f"    Bem vindo ao Word Quiz, {x} ")
    print("-----     1 Jogar      -----")
    print("-----     2 regras     -----")
    print("-----     3 sair       -----")    
    print("----------------------------")
    op = input(f"Qual opção deseja escolher,{x}?:")
    return op

def menu_1():
        global op_3
        while True:
            print("----------------------------")
            print("-----  Dificuldades    -----")
            print("-----  1-> Fácil       -----")
            print("-----  2-> Médio       -----")
            print("-----  3-> Díficil     -----")    
            print("----------------------------")
            op_3=input("Qual a dificuldade que deseja jogar?:")
            try:
                if op_3=="1":
                    logicafacil()
            except SyntaxError:
                print("Valor não pode ser inserido")
            
            try:    
                if op_3=="2":
                    logicamedia()
            except SyntaxError:
                print("Valor não pode ser inserido")
            
            try:    
                if op_3=="3":
                    logicadificil()
            except SyntaxError:
                print("Valor não pode ser inserido")
       
def menu_3():
    print("------------------------------------------")
    print("--- Agora tens 2 opções para escolher: ---")
    print("---          1-> Reiniciar             ---")
    print("---          2-> Sair                  ---")
    print("------------------------------------------")
    x=input("Qual das seguintes opções deseja escolher?:")
    if x=="1":
        menu_1()
    elif x=="2":
        return        
    
def menu_2():
        while True:
            print("---------------------------------------------------------------------")
            print("----------------------     REGRAS DO JOGO     -----------------------")
            print("---------------------------------------------------------------------")
            print("----- Esse jogo é um quiz onde se envolve conhecimento geral   ------")
            print("----- ele funciona da seguinte maneira possuí três dificuldades -----")    
            print("----- de acordo com o nível escolhido, o usuário irá receber um -----")
            print("----- número diferente de pontos sendo a mais fácil 1 ponto     -----")
            print("----- a média 2 pontos e a difícil 3 pontos. No final somaremos -----")
            print("----- todos os pontos de cada jogador e fazer um ranking.       -----")
            print("---------------------------------------------------------------------")
            print("-----                                                           -----")
            print("-----                                                           -----")
            print("---------------------------------------------------------------------")
            x=input("-------------- | Aperte enter para sair: | --------------")
            if x== "":
                 break

 
