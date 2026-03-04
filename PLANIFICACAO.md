# Projeto-Final-Python
Projeto final feito por Davi, Diogo e Bitar

## Como vamos apresentar as perguntas e memórias?:

- Nós iremos guardar as pergutas em 3 arquivos json diferentes, o facil.json, medio.json e dificil e dificil.json, essas perguntas serao guardadas em uma lista de dicionarios, em que irá ter a pergunta, as respostas guardadas dentro de um dicionario, o indice da resposta certa, e o nivel de dificuldade da pergunta.

ex:

```Python
[{
    "pergunta":"pergunta",
    "resposta":["resposta","resposta1","resposta2","resposta4"],
    "ressposta certa":1,
    "dificuldade":"dificil"
},
{
    "pergunta":"pergunta2",
    "resposta":["resposta2","resposta12","resposta22","resposta42"],
    "ressposta certa":3,
    "dificuldade":"dificil"
},
...
]
```


## Pontuação: programação e funcionamento

- A pontução será guarda e registrda por uma função. De acordo com seu nivel de dificuldade, será dado quantias de pontos diferentes [sendo distribuidos assim: Facil=1; Medio=2; Dificil=3.]

```Py
def dificuldade(*args):
    for  dif in args:
            if 
```
## 2) Entradas / Processamento / Saídas

#  entradas (o que o utilizador escreve / o que vem do JSON)

O utilizador irá escrever seu nome para poder ser identificado, após isso ele irá escrever a opção que deseja se escolher [por exemplo se quiser jogar vai escrever "1", se quiser escolher as regras "2" e etc];

ex:
```py
def menu_1():
        print("----------------------------")
        print("-----  DIFICULDADES    -----")
        print("-----  1-> Fácil       -----")
        print("-----  2-> Médio       -----")
        print("-----  67-> Díficil     -----")    
        print("----------------------------")
        x=input("qual a dificuldade que deseja?")
```

# processamento (o que o programa calcula/decide)

O programa vai mostrar o menu da difiuldade depois do utilizador escolher a opção de jogar, irá escolher a sua dificuldade em outro menu, ao escolher esse modo de dificuldade ele entrará no menu do quiz de perguntas gerais sobre aquela dificuldade, ao final do jogo o programa irá mostrar a sua pontuação, quantas perguntas acertou e a tabela de MVPS, 

# saídas (o que mostra no terminal / o que guarda em ficheiro)

No terminal mostrará uma frase a perguntas o seu nome, dara boas vindas e mostrara o menu principal do jogo, se clicar em regras mostra as regras, se clicar em sair acaba com a programação e se clicar em jogar vai escolher o modo de dificuldade, depois de escolher a dificuldade no menu de seleção de dificuldade vai mostrar o quiz para o jogador responder, no final irá mostrar se quer jogar novamente naquela mesma dificuldade, se quer jogar outra dificuldade, ou se quer sair do jogo (neste caso irá acabar com a execução do programa).

## 3) Lista de funções (com responsabilidades)

Estas serão as funções presentes:

- guardar_perguntas:salva as perguntas do jogo 

- mostrar_menu:mostrar as 3 opções do jogo, "jogar","regras","sair"

- soma_pontos: Faz a soma das pontuações das perguntas

- selecionar_dificuldade: seleciona as questoes do nivel quee a pessoa pede

- MVP: mostra as 3 melhores pessoas

## 4) Fluxo do programa

Quando o jogo inicia, a primeira coisa que irá aparecer ao utilizador será uma mensagem pedindo o seu nome, após isso terá uma mensagem de boas vindas com o respectivo nome que o usuário inseriu. Em seguida vai aparecer ao utilizador 3 opções, nessas opções estarão "Jogar", "Regras" e "Sair", o utilizador terá de escolher uma destas para assim poder continuar. Se o utlizador escolher jogar ele será transportando para o menu de dificuldades e lá terá de escolher a dificuldade que deseja, logo após isso ele será transportado para o jogo com a dificuldade que escolheu, no final de todo o jogo de perguntas e respostas irá ter de aparecer a quantidade de pontos, quantos pontos teve, o que acertou e errou e o MVP. No fim aparecerá uma opcão de jogar novamente, se quer jogar outro modo, ou uma opção de sair

## 5) Estrutura de ficheiros / módulos (decidida por vocês)

Para o trabalho utilizaremos dois tipos de ficheiro para o trabalho. O primeiro deles será o .py onde iremos fazer os modulos e usaremos os arquivos.json onde iremos salvar as informações

## 6) Plano de testes (manual)

Erros:

- Caso escolher uma letra errada (exemplo, a pessoa por Z ao invês de A);

- Caso a pessoa por um nome repitido ou não por nome trataremos como um erro;

- Caso a pessoa esccolha uma opçção errada no menu (exemplo se ao invês de por 1. Jogar a pessoa por um 5);

- Caso a pessoa escrever uma palavra ao invês da opção;

- Caso tenha um problema na hora de tratar os pontos;

- Caso fichero de perguntas não abrir;

- Caso a pontuação dadificuldade esteja errada

## 7) Mini-revisões antes de começar a programar

Mateus Bitar irá fazer o menu do jogo e a soma dos pontos, Diogo irá implementar as funções e programar a leitura dos arquivos json e Davi irá fazer outras funções tratamento de erros e guardar as perguntas em ficheiros json