import json
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
def perguntadificil():
    with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
        perguntas=json.load(f)


def perguntafacil():
    with (BASE_DIR / "facil.json").open("r",encoding="utf-8") as f:
        pergunta=json.load(f)


def perguntamedia():
    with (BASE_DIR / "medio.json").open("r",encoding="utf-8") as f:
        perguntado=json.load(f)


