import json
from logica import logicafacil,logicadificil,logicamedia

def menu(x):
    print("----------------------------")
    print(f"    BEM VINDO!!! {x} ")
    print("-----     1 Jogar      -----")
    print("-----     2 regras     -----")
    print("-----     3 sair       -----")    
    print("----------------------------")
    op = input("Qual a sua escolha?")
    return op


def menu_1():
        print("----------------------------")
        print("-----  DIFICULDADES    -----")
        print("-----  1-> Fácil       -----")
        print("-----  2-> Médio       -----")
        print("-----  67-> Díficil     -----")    
        print("----------------------------")
        op_3=input("qual a dificuldade que deseja?")
        if op_3=="1":
             logicafacil()
        elif op_3=="2":
             logicamedia()
        elif op_3=="67":
             logicadificil()
        
        

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
            x=input("-------------- | clique enter para continuar: | --------------")
            if x== "":
                 break



x=input("qual teu user: ")
while True:
    op=menu(x)
    if op=="1":
        op_1=menu_1()
    elif op=="2":
        op_2=menu_2()
    elif op=="3":
        print("foi um prazer ter você aqui presente no Word Quiz")
        break
 
 