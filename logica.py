import json
from lerperguntas import perguntadificil,perguntafacil,perguntamedia
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent

try:    
    def logicafacil():
        errou=0
        acertou=0
        pontos=0
        perguntas=perguntafacil()
        for dic in perguntas:
            print("---------------------------------------------------------------")
            print(dic['Pergunta'])
            print("---------------------------------------------------------------")
            for i in dic["Resposta"]:
                print(i)
            x=input("qual a resposta certa????????:")
            for u in dic["Correta"]:
                if x==u:
                    input("e tuuuu...............................")
                    input("ACERTASTE!!!!!!!!!!1")
                    acertou+=1
                    pontos+=2
                else:
                    input("e tuuuu...............................")
                    input("erraste parabens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! QUANDO PENSAVA QUE O ADEVERSARIO IAS SER TU")
                    errou+=1
            print("-----------------------------------------------------------------------------")
        print(f"-------------------------Parabens!!! acertaste {acertou}/20---------------------")
        print(f"-------------------------Mas erraste {errou}------------------------------------")
        print(f"-------------------------tiveste {pontos} pontos--------------------------------")
        print("---------------------------------------------------------------------------------")
except ValueError:
    print("Coloque um valor dentro dos pedidos")
except FileNotFoundError:
    print("Não é possivel abrir o ficheiro da dificuldade facil")


try:
    def logicamedia():
        errou=0
        acertou=0
        pontos=0
        perguntas=perguntamedia()
        for dic in perguntas:
            print("---------------------------------------------------------------")
            print(dic['Pergunta'])
            print("---------------------------------------------------------------")
            for i in dic["Resposta"]:
                print(i)
            x=input("qual a resposta certa????????:")
            for u in dic["Correta"]:
                if x==u:
                    input("e tuuuu...............................")
                    input("ACERTASTE!!!!!!!!!!1")
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
except ValueError:
    print("Coloque um valor dentro dos pedidos")
except FileNotFoundError:
    print("Não é possivel abrir o ficheiro da dificuldade media")



try:
    def logicadificil():
        errou=0
        acertou=0
        pontos=0
        perguntas=perguntadificil()
        for dic in perguntas:
            print("---------------------------------------------------------------")
            print(dic['Pergunta'])
            print("---------------------------------------------------------------")
            for i in dic["Resposta"]:
                print(i)
            x=input("qual a resposta certa????????:")
            for u in dic["Correta"]:
                if x==u:
                    input("e tuuuu...............................")
                    input("ACERTASTE!!!!!!!!!!1")
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
except ValueError:
    print("Coloque um valor dentro dos pedidos")
except FileNotFoundError:
    print("Não é possivel abrir o ficheiro da dificuldade dificil")


