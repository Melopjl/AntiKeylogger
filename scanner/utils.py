import json
from config import Config

def load_json(file_path=None):
    try:
        path = file_path or Config.SIGNATURE_FILE
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}
