import json
import lerperguntas
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent

with (BASE_DIR / "facil.json").open("r",encoding="utf-8") as f:
    perguntas=json.load(f)

for dic in perguntas:
    print("---------------------------------------------------------------")
    print(dic['Pergunta'])
    print("---------------------------------------------------------------")
    for i in dic["Resposta"]:
        print(i)
    print("---------------------------------------------------------------")
       