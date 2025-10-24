ETAPES DE REALISATION DU PROJRT
++++++++++++++++++++++++++++++++++
DATA 
=====================================
**1. Collecte de Données depuis Hugging Face**
   -------------------------------------------------
   La première étape a consisté à récupérer des données pertinentes sur les maladies cardiaques à partir de la plateforme Hugging Face. Ces données incluent des jeux d'informations liées à la santé, comme les symptômes, les facteurs de risque et les traitements.

**2. Fusion des Données dans un Fichier Unique**
   -------------------------------------------------
   Fusiommer toutes les données collectées ont été  dans un seul fichier CSV pour une gestion centralisée. Cela a permis une organisation optimale avant de procéder aux étapes suivantes.

**3. Nettoyage des Données**
   ----------------------------
    en supprimant les doublons, les informations inutiles et les incohérences, et en estimant les veluers monqunates 

**4. Création des Questions et Réponses**
   ------------------------------------------
   
   Des questions et réponses ont été générées à partir des données nettoyées , apres on tramsfomes ces dialogues en un fichier PDF.
Base de vecteurs
=====================================
**5. Création d'une Base de Vecteurs avec ChromaDB**
   --------------------------------------------------
   En utlisant  ChromaDB et le modèle `mxbai-embed-large` on cree une base de veteurs ce qui permet de rechercher efficacement les informations pertinentes à partir des données indexées.

RAG
=====================================
**6. La politique du rèponse et le modles RAG**
   ----------------------------------------------------
   Cette etpaes conciste a préciser la stratégie de récupération des informations  à partir de la base de veteurs 
   et de faire la gestion des cas où aucune réponse pertinente n'est trouvée c'est  à dire si la similarité des documents est trop faible, le Chatbot retourne une réponse par défaut comme :
   "Je suis désolé, je ne trouve pas d'information pertinente dans ma base de données. Pouvez-vous reformuler votre question ?"

Streamlit
=====================================
**7. developpemenet de l'interface du Chatbot sur streamlit:**
   ---------------------------------------------------------
   Pour creer interface conviviale et interactive, permettant une expérience utilisateur fluide.
   