import json
import lerperguntas
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent

with (BASE_DIR / "dificil.json").open("r",encoding="utf-8") as f:
    perguntas=json.load(f)
    

