import json
from logica import logicafacil,logicadificil,logicamedia
algo=True

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
        print("-----  3-> Díficil     -----")    
        print("----------------------------")
        op_3=input("qual a dificuldade que deseja?")
        try:
            if op_3=="1":
                logicafacil()
                print("agora,tens 3 opções,pressionar enter para reiniciar neste modo, escreva retornar para retornar para as dificudades,  ")
                input("e escreve sair para sair do jogo")
                final=input("qual opção queres???:")
                while algo:
                    if final=="":
                        logicafacil()
                        break
                    if final=="retornar":
                        menu_1()
                    if final=="sair":
                        break
        except SyntaxError:
            print("Valor não pode ser inserido")
        
        try:    
            if op_3=="2":
                logicamedia()
                print("agora,tens 3 opções,pressionar enter para reiniciar neste modo, escreva retornar para retornar para as dificudades,  ")
                input("e escreve sair para acabar com o jogo")
                final=input("qual opção queres???:")
                while algo:
                    if final=="":
                        logicamedia()
                    if final=="retornar":
                        menu_1()
                    if final=="sair":
                        break
        except SyntaxError:
            print("Valor não pode ser inserido")
        
        try:    
            if op_3=="3":
                logicadificil()
                print("agora,tens 3 opções,pressionar enter para reiniciar neste modo, escreva retornar para retornar para as dificudades,  ")
                input("e escreve sair para acabar com o jogo")
                final=input("qual opção queres???:")
                while algo:
                    if final=="":
                        logicadificil()
                    if final=="retornar":
                        menu_1()
                    if final=="sair":
                        break 
        except SyntaxError:
            print("Valor não pode ser inserido")
       
        
    
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

 
 