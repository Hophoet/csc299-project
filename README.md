# TP-final-IPNet-2019-2020
Travaux pratiques de Lab informatique destinés aux étudiants de Licence 4 à IPNet Institute.

## Développement d'une API de gestion des contacts : 
- API
- Test unitaires
- Intégration continue
- Sécurité : authentification avec token des utilisateurs
- Outils: 
   - Python
   - FastAPI
   - SQLite
   - Heroku
   - Github
   - Uvicorn
   
## Endpoints
Les endpoints suivants sont fondamentaux. D'autres qui sont jugés utiles sont vivement encouragés.

- /contacts/?d=0&f=20 : liste des (f-d) premiers contacts à compter de d.
- /entreprises/?d=0&f=20 : liste des (f-d) premières entreprises à compter de d.
- /secteurs/?d=0&f=20 : liste des (f-d) premiers secteurs à compter de d.
- /recherche/?q=query : recherche du terme q
- /contact/id/ : contact dont l'identifiant est id
- /entreprise/id/ : entreprise dont l'identifiant est id
- /secteur/id/ : secteur dont l'identifiant est id


## Travail demandé :

Mettre en oeuvre une API de gestion des contacts. Les contacts travaillent dans une entreprise exerçant dans un secteur d'activité.
Il est attendu de votre part de développer cette API, en mettant en oeuvre les tests unitaires, et configurer l'intégration continue avec Github Actions et le déployer sur Heroku.
Libre à vous d'utiliser la base de données qui convient.
