import json
from menu import menu,menu_1,menu_2,algo

try:
    x=input("Escreva o seu nome: ")
    while True:
        op=menu(x)
        if op=="1":
            op_1=menu_1()
        elif op=="2":
            op_2=menu_2()
        elif op=="3":
            print("Foi um prazer ter você aqui presente no Word Quiz")
            break
        if algo==False:
            break
except SyntaxError:
            print("Valor não pode ser inserido")
