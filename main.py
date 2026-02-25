import json
import menu

x=input("introduz o seu nome de usuario para o word quiz:")
print("------------------------------------------------")
print(f"BOAS VINDAS,{x}, AO WORD QUIZ")
print("1->  Jogar  <-")
print("2->  regras <-")
print("3->  sair   <-")
print("------------------------------------------------")
y=input("qual é a opcão que vc deseja?")
print("------------------------------------------------")

menu.jogar(y)
menu.regras(y)
menu.sair(y)
