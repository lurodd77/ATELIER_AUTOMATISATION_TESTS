🚀 Mon projet — API Monitoring Frankfurter
API choisie
API : Frankfurter
Type : API de taux de change
Authentification : Aucune
URL de base : https://api.frankfurter.dev
Documentation : https://frankfurter.dev/
🧪 Tests automatisés

J'ai développé une solution permettant de tester automatiquement l'API Frankfurter.

6 tests sont exécutés :

Vérification du code HTTP 200
Vérification du Content-Type JSON
Vérification des champs obligatoires
Vérification du type des champs
Vérification des valeurs EUR/USD
Vérification du comportement avec une devise invalide

Les tests sont non destructifs et utilisent uniquement des requêtes GET.

🛡️ Robustesse

Le client HTTP possède :

Timeout de 3 secondes
1 retry maximum
Gestion du code HTTP 429
Gestion des erreurs serveur 5xx
Gestion des timeouts et erreurs réseau
📊 Métriques QoS

Pour chaque exécution, les indicateurs suivants sont calculés :

Nombre de tests réussis
Nombre de tests échoués
Taux d'erreur
Disponibilité
Latence moyenne
Latence P95

Exemple d'un résultat obtenu :

Tests : 6
PASS : 6
FAIL : 0
Disponibilité : 100 %
Taux d'erreur : 0 %
Latence moyenne : 108.03 ms
P95 : 305.48 ms
💾 Historique

Les résultats des exécutions sont enregistrés dans une base de données SQLite afin de conserver un historique.

🌐 Application Flask

L'application expose plusieurs routes :

/run : lance les tests et enregistre les résultats
/dashboard : affiche les métriques et l'historique
/health : indique l'état de santé de la solution
🏗️ Architecture
project/
├── flask_app.py
├── storage.py
├── API_CHOICE.md
├── requirements.txt
├── tester/
│   ├── client.py
│   ├── tests.py
│   └── runner.py
└── templates/
    └── dashboard.html
☁️ Déploiement

L'application est déployée sur PythonAnywhere.

Le déploiement est automatisé avec GitHub Actions à chaque modification du repository.

✅ Résultat

La solution permet de :

Tester → Mesurer → Enregistrer → Surveiller

l'API publique Frankfurter.

------------------------------------------------------------------------------------------------------
🎯Atelier “Testing as Code & API Monitoring”
------------------------------------------------------------------------------------------------------
Rodrigues Lucas
Aujourd’hui, vous allez passer du rôle de développeur au rôle d’ingénieur qualité.  
  
Internet est rempli d’API publiques : météo, devises, citations, géolocalisation, données statistiques…
Mais une API, ce n’est pas juste une URL qui répond. C’est un service.
Et un service doit être fiable, mesurable et surveillé.  
  
Votre mission :  
  
👉 Choisir une API publique.  
👉 Concevoir et implémenter une solution d’automatisation des tests.  
👉 Déployer votre solution sur PythonAnywhere.  
👉 Mesurer et exposer des indicateurs de qualité de service.    
  
-------------------------------------------------------------------------------------------------------
🧩 Séquence 1 : GitHUB
-------------------------------------------------------------------------------------------------------
Objectif : Création d'un Repository GitHUB pour travailler avec son projet  
Difficulté : Très facile (~10 minutes)
-------------------------------------------------------------------------------------------------------
**Faites un Fork de ce projet**. Si besoin, voici une vidéo d'accompagnement pour vous aider à "Forker" un Repository Github : [Forker ce projet](https://youtu.be/p33-7XQ29zQ)  

---------------------------------------------------
🧩 Séquence 2 : Création d'un site chez Pythonanywhere
---------------------------------------------------
Objectif : Créer un hébergement sur Pythonanywhere  
Difficulté : Faible (~10 minutes)
---------------------------------------------------

Rendez-vous sur **https://www.pythonanywhere.com/** et créez vous un compte. Puis créez un serveur Web **Flask 3.13**. 
  
---------------------------------------------------------------------------------------------
🧩 Séquence 3 : Les Actions GitHUB (Industrialisation Continue)
---------------------------------------------------------------------------------------------
Objectif : Automatiser la mise à jour de votre hébergement Pythonanywhere  
Difficulté : Moyenne (~15 minutes)
---------------------------------------------------------------------------------------------
Dans le Repository GitHUB que vous venez de créer précédemment lors de la séquence 1, vous avez un fichier intitulé deploy-pythonanywhere.yml et qui est déposé dans le répertoire .github/workflows. Ce fichier a pour objectif d'automatiser le déploiement de votre code sur votre site Pythonanywhere. Pour information, c'est ce que l'on appel des Actions GitHUB. Ce sont des scripts qui s'exécutent automatiquement lors de chaque Commit dans votre projet (C'est à dire à chaque modification de votre code). Ces scripts (appelés actions) sont au format yml qui est un format structuré proche de celui d'XML.  

Pour utiliser cette Action (deploy-pythonanywhere.yml), **vous avez besoin de créer des secrets dans GitHUB** afin de ne pas divulguer des informations sensibles aux internautes de passage dans votre Repository comme vos login et password par exemple.  

Pour cet atelier, **vous avez 4 secrets à créer** dans votre Repository GitHUB : **Settings → Secrets and variables → Actions → New repository secret**  
  
**PA_USERNAME** = votre username PythonAnywhere.  
**PA_TOKEN** = votre API token. Token à créer dans pythonanywhere (Acount → API Token).  
**PA_TARGET_DIR** = Web → Source code (ex: /home/monuser/myapp).  
**PA_WEBAPP_DOMAIN** = votre site (ex: monuser.pythonanywhere.com).  
  
**Dernière étape :** Pour engager l'automatisation de votre première Action, vous devez cliquer sur le gros boutton vert dans l'onglet supérieur [Actions] dans votre Repository Github. Le boutton s'intitule "I understand my workflows, go ahead and enable them". Ensuite procédez à une "petite" modification de votre fichier README.md GitHub puis faites un [Commit] pour déclancher l'action.   

Notions acquises de cette séquence :  
Vous avez vu dans cette séquence comment créer des secrets GiHUB afin de mettre en place de l'industrialisation continue.   
  
---------------------------------------------------
🔹 Séquence 4 : Atelier
---------------------------------------------------
Objectif : Travailler sur l'automatisation de vos tests  
Difficulté : Moyenne (~120 minutes)
---------------------------------------------------
**Consignes : Retrouvez les consignes de votre atelier sur votre site pythonanywhere**    
Vous pouvez retrouver le travail demandé dans le cadre de cet atelier directement sur votre site pythonanywhere (ex: monuser.pythonanywhere.com).    
   
--------------------------------------------------------------------
🧠 Troubleshooting :
---------------------------------------------------
Objectif : Visualiser ses logs et découvrir ses erreurs
---------------------------------------------------
Lors de vos développements, vous serez peut-être confronté à des erreurs systèmes car vous avez faits des erreurs de syntaxes dans votre code, faits de mauvaises déclarations de fonctions, appelez des modules inexistants, mal renseigner vos secrets, etc…  
Les causes d'erreurs sont quasi illimitées. **Vous devez donc vous tourner vers les logs de votre système pour comprendre d'où vient le problème** :  

Vos log sont accéssible via les URL suivantes :  
* Access log : {site}.pythonanywhere.com.access.log
* Error log : {site}.pythonanywhere.com.error.log
* Server log: {site}.pythonanywhere.com.server.log
