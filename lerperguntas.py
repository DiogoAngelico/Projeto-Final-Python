import json
from pathlib import Path
import random

BASE_DIR=Path(__file__).resolve().parent

try:
    def perguntafacil():
        listaaleatoria=[]
        x=0
        with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
            perguntas=json.load(f)
        while x<10:
            pergunta_random=random.choice(perguntas)
            if pergunta_random in listaaleatoria:
                continue
            else:
                listaaleatoria.append(pergunta_random)
                x+=1
        return listaaleatoria
    
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

try:
    def perguntamedia():
        listaaleatoria=[]
        x=0
        with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
            perguntas=json.load(f)
        while x<10:
            pergunta_random=random.choice(perguntas)
            if pergunta_random in listaaleatoria:
                continue
            else:
                listaaleatoria.append(pergunta_random)
                x+=1
        return listaaleatoria
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

try:
    def perguntadificil():
        listaaleatoria=[]
        x=0
        with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
            perguntas=json.load(f)
        while x<10:
            pergunta_random=random.choice(perguntas)
            if pergunta_random in listaaleatoria:
                continue
            else:
                listaaleatoria.append(pergunta_random)
                x+=1
        return listaaleatoria
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

