#  Football Pipeline (API football-data.org)

## Description
Pipeline ETL automatisé qui extrait des données depuis l'API football-data.org,
les transforme et les stocke dans une base de données SQLite pour produire
des insights sur les 5 plus grands championnats d'Europe et la Champions League (classement équipes, meilleurs buteurs,  résultats de matchs).

## Technologies utilisées

- **requests** — envoyer des requêtes HTTP à l'API football
- **pandas** — nettoyer et transformer les données brutes en tableaux structurés
- **schedule** — automatiser l'exécution quotidienne du pipeline
- **python-dotenv** — charger la clé API depuis un fichier .env de manière sécurisée
- **venv** — environnement virtuel Python qui isole les dépendances du projet
  pour éviter les conflits entre les bibliothèques de différents projets

## Installation

### 1. Cloner le projet
```bash
git clone <url-du-repo>
cd football_pipeline
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la clé API
Crée un fichier `.env` à la racine du projet :
API_KEY=ta_clé_api


## Lancer le pipeline
```bash
python pipeline.py
```

## Structure du projet
football_pipeline/
├── config.py       # Configuration et variables globales
├── extract.py      # Appels à l'API football-data.org
├── transform.py    # Nettoyage et transformation avec pandas
├── load.py         # Insertion des données en base SQLite
├── queries.py      # Requêtes analytiques SQL
├── football.db      # Base de donnée SQLite (générée automatiquement)
├── pipeline.py     # Orchestration + scheduling quotidien
├── .env            # Clé API (génère ta clé sur football-data.org )
└── .gitignore      # Fichiers ignorés par Git




## Analyses générées  Champions League et dans les 5 grands championnats d'Europe

-  Top 5 équipes au classement
-  Top 5 équipes avec le plus de buts marqués
-  Top 5 matchs avec le plus de buts
-  Top 5 meilleurs buteurs 
