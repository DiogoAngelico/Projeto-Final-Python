import json
import selecionar_dificuldade

def jogar(y):
    if y == "1":
        print("----------------------")
        print("  dificuldades  ")
        print("1-> dificil <-")
        print("2->  médio  <-")
        print("3->  fácil  <-")
        print("----------------------")
        

def regras(y):
    if y == "2":
        print(f"Esse quiz envolve conhecimento geral, em três níveis de dificuldades, dando pontos diferentes de acordo com a dificuldade, caso seja selecionada, na dificuldade difícil irá ganhar 3 ponto por cada pergunta correta, no médio são 2 ponto por cada pergunta correta, fácil ganhará 1 ponto só, importante saber que iremos hackear as pessoas com maiores pontuações, escolher com sabedoria o nível a qual irá jogar, são 20 perguntas pra cada dificuldade" )
                
def sair(y):
    if y == "3":
        print(f"Foi um prazer ter você com a gente")
              
'''     
def sair(y):
    if y == "3":
'''        