import json
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent

try:
    def perguntadificil():
        with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
            perguntas=json.load(f)
        return perguntas
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

try:
    def perguntafacil():
        with (BASE_DIR / "facil.json").open("r",encoding="utf-8") as f:
            pergunta=json.load(f)
        return pergunta
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

try:
    def perguntamedia():
        with (BASE_DIR / "medio.json").open("r",encoding="utf-8") as f:
            perguntado=json.load(f)
        return perguntado
except FileNotFoundError:
    print("Não foi encontrado nenhum arquivo")

