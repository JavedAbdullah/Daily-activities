import os
import datetime
import subprocess

# === CONFIGURAZIONE ===
repo_path = os.path.dirname(os.path.abspath(__file__))
file_name = "attività.txt"
file_path = os.path.join(repo_path, file_name)

# === DATI DI OGGI ===
today = datetime.datetime.now().strftime("%Y-%m-%d")
commit_message = f"Update attività: {today}"

# === ATTIVITÀ DA AGGIUNGERE ===
attività = [
    "- finire Step 2 di Sweng",
    "- fare un esercitazione di NA",
    "- fare AMSC",
    "- rivedere pensare al prossimo post di LINKLDN"
]

# === CREA O AGGIORNA IL FILE ===
with open(file_path, "a", encoding="utf-8") as f:
    f.write(f"\n====== {today} ======\n")
    for item in attività:
        f.write(item + "\n")

# === COMANDI GIT ===
commands = [
    ["git", "-C", repo_path, "add", file_name],
    ["git", "-C", repo_path, "commit", "-m", commit_message],
    ["git", "-C", repo_path, "push"]
]

for cmd in commands:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante '{' '.join(cmd)}': {e}")
