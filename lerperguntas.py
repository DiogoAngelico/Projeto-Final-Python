import json
from pathlib import Path
import random

BASE_DIR=Path(__file__).resolve().parent

def perguntafacil():
    try:
        listaaleatoria=[]
        x=0
        with (BASE_DIR / "facil.json").open("r",encoding="utf-8") as f:
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

def perguntamedia():
    try:
        listaaleatoria=[]
        x=0
        with (BASE_DIR / "medio.json").open("r",encoding="utf-8") as f:
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

def perguntadificil():
    try:
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

