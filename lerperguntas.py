import json

def ler_perguntas():
    with open("guardar_perguntas.json","r", encoding="utf-8") as F:
        perguntas=json.load(F)

