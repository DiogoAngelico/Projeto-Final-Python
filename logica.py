import json
from lerperguntas import perguntadificil,perguntafacil,perguntamedia
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
def logicafacil():
    errou=0
    acertou=0
    pontos=0
    algo=True
    perguntas=perguntafacil()
    for dic in perguntas:
        print("---------------------------------------------------------------")
        print(dic['Pergunta'])
        print("---------------------------------------------------------------")
        for i in dic["Resposta"]:
            print(i)
        x=int(input("qual a resposta certa????????:"))
        for u in dic["Correta"]:
            if x==u:
                print("e tuuuu...............................")
                print("ACERTASTE!!!!!!!!!!1")
                acertou+=1
                pontos+=2
            else:
                input("e tuuuu...............................")
                input("erraste parabens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! QUANDO PENSAVA QUE O ADEVERSARIO IAS SER TU")
                errou+=1
        print("---------------------------------------------------------------")
    print(f"Parabens!!! acertaste {acertou}/20")
    print(f"Mas erraste {errou}")
    print(f"tiveste {pontos} pontos!")



def logicamedia():
    errou=0
    acertou=0
    pontos=0
    algo=True
    perguntas=perguntamedia()
    for dic in perguntas:
        print("---------------------------------------------------------------")
        print(dic['Pergunta'])
        print("---------------------------------------------------------------")
        for i in dic["Resposta"]:
            print(i)
        x=int(input("qual a resposta certa????????:"))
        for u in dic["Correta"]:
            if x==u:
                print("e tuuuu...............................")
                print("ACERTASTE!!!!!!!!!!1")
                acertou+=1
                pontos+=2
            else:
                input("e tuuuu...............................")
                input("erraste parabens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! QUANDO PENSAVA QUE O ADEVERSARIO IAS SER TU")
                errou+=1
        print("---------------------------------------------------------------")
    print(f"Parabens!!! acertaste {acertou}/20")
    print(f"Mas erraste {errou}")
    print(f"tiveste {pontos} pontos!")

def logicadificil():
    errou=0
    acertou=0
    pontos=0
    algo=True
    perguntas=perguntadificil()
    for dic in perguntas:
        print("---------------------------------------------------------------")
        print(dic['Pergunta'])
        print("---------------------------------------------------------------")
        for i in dic["Resposta"]:
            print(i)
        x=int(input("qual a resposta certa????????:"))
        for u in dic["Correta"]:
            if x==u:
                print("e tuuuu...............................")
                print("ACERTASTE!!!!!!!!!!1")
                acertou+=1
                pontos+=2
            else:
                input("e tuuuu...............................")
                input("erraste parabens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! QUANDO PENSAVA QUE O ADEVERSARIO IAS SER TU")
                errou+=1
        print("---------------------------------------------------------------")
    print(f"Parabens!!! acertaste {acertou}/20")
    print(f"Mas erraste {errou}")
    print(f"tiveste {pontos} pontos!")


logicafacil()
logicamedia()
logicadificil()