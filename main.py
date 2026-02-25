import menu
import json


x=input("qual teu user: ")
while True:
    op=menu.menu(x)
    if op=="1":
        op_1=menu.menu_1()
    elif op=="2":
        op_2=menu.menu_2()
    elif op=="3":
         print("foi um prazer ter você aqui presente no Word Quiz")
         break
        