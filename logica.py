import json
from lerperguntas import perguntadificil,perguntafacil,perguntamedia
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
import random

    
def logicafacil():
    try:
        variavel=0
        errou=0
        acertou=0
        pontos=0
        perguntas=perguntafacil()
        while variavel<10:
            for dic in perguntas:
                print("---------------------------------------------------------------")
                print(dic['Pergunta'])
                print("---------------------------------------------------------------")
                for i in dic["Resposta"]:
                    print(i)
                x=input("qual a resposta certa?:")
                for u in dic["Correta"]:
                    if x==u:
                        input("Acertaste")
                        acertou+=1
                        pontos+=1
                        variavel+=1
                    else:
                        input("Erraste")
                        errou+=1
                        variavel+=1
                if variavel==10:
                    break               
        print("---------------------------------------------------------------------------------")
        print(f"-------------------------Parabens! acertaste {acertou}/10------------------------")
        print(f"-------------------------Mas erraste {errou}-------------------------------------")
        print(f"-------------------------Tiveste {pontos} pontos---------------------------------")
        print("---------------------------------------------------------------------------------")
    except ValueError:
        print("Coloque um valor dentro dos pedidos")
    except FileNotFoundError:
        print("Não é possivel abrir o ficheiro da dificuldade facil")


def logicamedia():
    try:
        errou=0
        acertou=0
        pontos=0
        variavel=0
        perguntas=perguntamedia()
        while variavel<10:
            for dic in perguntas:
                print("---------------------------------------------------------------")
                print(dic['Pergunta'])
                print("---------------------------------------------------------------")
                for i in dic["Resposta"]:
                    print(i)
                x=input("qual a resposta certa?:")
                for u in dic["Correta"]:
                    if x==u:
                        input("Acertaste")
                        acertou+=1
                        pontos+=2
                        variavel+=1
                    else:
                        input("Erraste")
                        errou+=1
                        variavel+=1
                if variavel==10:
                    break
        print("---------------------------------------------------------------------------------")
        print(f"--------------------------Parabens! acertaste {acertou}/10-----------------------")
        print(f"--------------------------Mas erraste {errou}------------------------------------")
        print(f"--------------------------Tiveste {pontos} pontos--------------------------------")
        print("---------------------------------------------------------------------------------")
    except ValueError:
        print("Coloque um valor dentro dos pedidos")
    except FileNotFoundError:
        print("Não é possivel abrir o ficheiro da dificuldade media")



def logicadificil():
    try:
        errou=0
        acertou=0
        pontos=0
        variavel=0
        perguntas=perguntadificil()
        while variavel<10:
            for dic in perguntas:
                print("---------------------------------------------------------------")
                print(dic['Pergunta'])
                print("---------------------------------------------------------------")
                for i in dic["Resposta"]:
                    print(i)
                x=input("qual a resposta certa?:")
                for u in dic["Correta"]:
                    if x==u:
                        input("Acertaste")
                        acertou+=1
                        pontos+=3
                        variavel+=1
                    else:
                        input("Erraste")
                        errou+=1
                        variavel+=1
                if variavel==10:
                    break
        print("---------------------------------------------------------------------------------")
        print(f"---------------------------Parabens! acertaste {acertou}/10----------------------")
        print(f"--------------------------Mas erraste {errou}------------------------------------")
        print(f"--------------------------Tiveste {pontos} pontos--------------------------------")
        print("---------------------------------------------------------------------------------")
    except ValueError:
        print("Coloque um valor dentro dos pedidos")
    except FileNotFoundError:
        print("Não é possivel abrir o ficheiro da dificuldade dificil")


