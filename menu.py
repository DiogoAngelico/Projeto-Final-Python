
def menu(x):
    print("---------------------------")
    print(f"    BEM VINDO!!! {x} ")
    print("-----     1 Jogar      -----")
    print("-----     2 regras     -----")
    print("-----     3 sair       -----")    
    print("---------------------------")
    op = input("Qual a sua escolha?")
    return op


def menu_1():
        print("---------------------------")
        print("-----  DIFICULDADES   -----")
        print("-----  1-> Fácil       -----")
        print("-----  2-> Médio       -----")
        print("-----  67-> Díficil     -----")    
        print("---------------------------")
        x=input("qual a dificuldade que deseja?")
        

def menu_2():
        while True:
            print("----------------------------------")
            print("-----     REGRAS DO JOGO     -----")
            print("-----                        -----")
            print("-----                        -----")    
            print("-----                        -----")
            print("-----                        -----")
            print("-----                        -----")
            print("-----                        -----")
            print("-----                        -----")
            print("-----                        -----")
            print("----------------------------------")
            x=input("clique enter para continuar:")
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
        