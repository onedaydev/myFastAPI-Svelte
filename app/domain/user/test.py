import os, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

SECRET_KEY = secrets['SECRET_KEY']
print(SECRET_KEY)