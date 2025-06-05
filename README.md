# 🔐 Darkly – Projet de Pentesting (École 42)

Projet de groupe réalisé avec [Malo Lefort](https://github.com/Malolfrt)

**Darkly** est un projet de sécurité web réalisé dans le cadre de ma formation à l'École 42. L'objectif principal est d'identifier et d'exploiter 14 failles de sécurité présentes sur un site web hébergé sur une machine virtuelle. Chaque faille permet de récupérer un **flag**, pour un total de 14 flags.

## 🧠 Objectif

Le but de ce projet est de mettre en pratique des compétences en **sécurité web**, en identifiant des vulnérabilités courantes, en les exploitant de manière contrôlée dans un environnement prévu à cet effet et savoir comment s'en protéger.

---

## 🛡️ Liste des failles exploitées

### 1. Admin_htpasswd
Accès non autorisé au fichier `.htpasswd`, contenant les identifiants chiffrés, permettant de récupérer le mot de passe de l'administrateur.

### 2. Cookies
Modification d’un cookie `admin` encodé en **MD5**, pour obtenir un accès privilégié.

### 3. File Upload
Utilisation de `curl` pour contourner la restriction d’extension et téléverser un fichier `.php` alors que seuls les fichiers `.jpg/.jpeg` sont autorisés via l'interface web.

### 4. Include
Faille de type **Local File Inclusion (LFI)** permettant d’accéder à `/etc/passwd` via l’URL.

### 5. Recover password
Changement du mot de passe via la page de récupération sans validation du mail d’origine.

### 6. Spoof_url
Altération des headers HTTP `Referer` et `User-Agent` pour contourner un mécanisme de protection et récupérer un flag.

### 7. SQL Injection (Basique)
Injection SQL simple (`1' OR 1=1 -- `) permettant de bypasser une authentification ou d'extraire des données.

### 8. SQL Injection (Avancée)
Injection plus complexe avec UNION SELECT, sous-requêtes ou time-based blind SQL.

### 9. XSS (Basique - Stored)
Injection JavaScript simple dans un champ non protégé pour exécuter du code malveillant.

### 10. XSS (Avancé - Reflected)
Exécution de code JavaScript encodé en **Base64** via un paramètre URL pour déclencher une alerte ou voler un cookie.

### 11. Brute Force
Script automatisé de **brute-force** sur un formulaire de connexion pour récupérer un mot de passe.

### 12. Hidden File
Création d’un script pour détecter des fichiers cachés dans un répertoire `.hidden`.

### 13. Redirect
Injection d’un lien malveillant pour rediriger l’utilisateur vers un site externe non autorisé (**Open Redirect**).

### 14. Survey
Modification directe dans la console du navigateur pour augmenter artificiellement le nombre de votes (autorisé initialement de 1 à 10).

---

## 🧰 Outils utilisés

- `curl`
- Burp Suite
- Navigateur avec DevTools
- Scripts bash/python (scraping, brute force, etc...)
