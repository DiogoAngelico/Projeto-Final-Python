# Projeto-Final-Python
Projeto final feito por Davi, Diogo e Bitar

## Como vamos apresentar as perguntas e memórias?:

- Nós iremos guardar as pergutas em um dicionario onde também estarão as respostas em formato de lista (apresentadas por A, B, C, D), de forma simplificada usaremos dicionarios e listas; 

ex:

```Python
dicionario={
    "pergunta":"pergunta",
    "resposta":["resposta","resposta1","resposta2","resposta4"],
    "ressposta certa":1,
    "dificuldade":"dificil"
}
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

O utilizador irá escrever seu nome para poder ser identificado, após isso ele irá escrever a opção que deseja se escolher [por exemplo se quiser jogar vai escrever "1", se for escolher a opção ele irá escrever "A"];

# processamento (o que o programa calcula/decide)

O programa vai calcular as perguntas que serão geradas automaticamente, calcular quantos pontos terá a pergunta e calcular quantos pontos a pessoa poderia ter e quantos ela teve;

# saídas (o que mostra no terminal / o que guarda em ficheiro)

No terminal estara as opções, de "jogar", "regras" e "sair", com no fim estando presente os creditos dos criadores. Será guardado em fichero onde vai ser calculado os pontos, os nomes dos usúarios e os erros;

## 3) Lista de funções (com responsabilidades)

Estas serão as funções presentes:

- guardar_perguntas:salva as perguntas do jogo 

- mostrar_menu:mostrar as 3 opções do jogo, "jogar","regras","sair"

- soma_pontos: Faz a soma das pontuações das perguntas

- selecionar_dificuldade: seleciona as questoes do nivel quee a pessoa pede

- MVP: mostra as 3 melhores pessoas

## 4) Fluxo do programa

Quando o jogo inicia, a primeira coisa que irá aparecer ao utilizador será uma mensagem pedindo o seu nome, apóos isso terá uma mensagem de boas vindas com o respectivo nome que o usuário inseriu. Em seguida vai aparecer ao utilizador 3 opções, nessas opções estarão "Jogar", "Regras" e "Sair", o utilizador terá de escolher uma destas para assim poder continuar. Se o utlizador escolher jogar ele será transportando para o menu de dificuldades e lá terá de escolher a dificuldade que deseja, logo após isso ele será transportado para o jogo com aa dificuldade que escolheu, no final de todo o jogo de perguntas e respostas irá ter de aparecer a quantidade de pontos, quantos pontos teve, o que acertou e errou e o MVP. No fim aparecerá uma opcão de jogar novamente ou uma opção de sair

## 5) Estrutura de ficheiros / módulos (decidida por vocês)

Para o trabalho utilizaremos dois tipos de ficheiro para o presente projeto e trabalho. O primeiro deles será o .py onde iremos fazer os modulos enquanto o sefundo por sua vez será o .json onde iremos salvar as informações

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

Mateus Bitar irá fazer o menu do jogo, Diogo irá implementar as funções e Davi irá fazer o tratamento de erros