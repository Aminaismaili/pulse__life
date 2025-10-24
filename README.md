# Mon projet
#  Chatbot des Maladies Cardiaques – *Project1*

### 🧠 Intelligence Artificielle pour la Santé Cardiaque  
**Encadrant :** [Masrour Tawfik](https://www.linkedin.com/in/tawfik-masrour-43163b85/)  
**Équipe du projet :**  
-  **Alae Boutarhat**  
-  **Amina Ismaili**

---

## 📘 Description du Projet

Le **Chatbot des Maladies Cardiaques** est une solution intelligente conçue pour **aider à la prévention, à la sensibilisation et à la gestion** des maladies cardiovasculaires.  
Basé sur des **modèles de langage avancés (LLM)** et des **pipelines IA modernes**, ce projet fournit des **réponses personnalisées, fiables et éducatives** selon les besoins de chaque utilisateur.

---

## 🚀 Objectifs

- **🎓 Sensibiliser** le public aux risques des maladies cardiaques.  
- **📚 Rendre accessible** l’information médicale de manière simple et interactive.  
- **🤝 Accompagner** les patients dans leur suivi et leur gestion de santé.  
- **💬 Favoriser** une interaction fluide et naturelle entre l’utilisateur et le chatbot.

---

## ⚙️ Caractéristiques Principales

| Fonctionnalité | Description |
|----------------|--------------|
| 🩺 **Analyse des données médicales** | Interprète les dossiers médicaux pour offrir des conseils personnalisés. |
| 🔍 **Génération augmentée (RAG)** | Combine recherche documentaire et génération de texte pour fournir des réponses fiables. |
| 🏥 **Localisation des services** | Propose les hôpitaux et centres de santé les plus proches. |
|  **Conseils sur la santé cardiaque** | Fournit des recommandations basées sur des données cliniques. |

---

## 🧩 Technologies Clés

| Domaine | Technologie |
|----------|-------------|
| 🔠 **Modèles de Langage (LLM)** | Mistral, RAG, MXBAI |
| 🔍 **Recherche sémantique** | Dense Passage Retriever (DPR), TransformersReader |
| 🧠 **Vectorisation** | ChromaDB + modèle `mxbai-embed-large` |
| 💻 **Interface Utilisateur** | [Streamlit](https://streamlit.io) |
| 📦 **Outils Python** | `langchain`, `transformers`, `chromadb`, `pypdf`, `faiss`, `sentence-transformers` |

---

## 🧪 Pipeline de Développement

1. **Collecte des données** depuis Hugging Face : symptômes, traitements, facteurs de risque.  
2. **Fusion et nettoyage** des données dans un fichier PDF unique.  
3. **Génération de dialogues** Q/R pour entraîner le chatbot.  
4. **Création d’une base vectorielle** via ChromaDB pour la recherche sémantique.  
5. **Développement du chatbot** :
   - Modèle **Mistral** pour la génération contextuelle.
   - Interface **Streamlit** interactive et moderne.  

---

## 🧭 Architecture du Projet

```
ChatbotPulseLife-main/
│
├── app/                         # Application Streamlit
│   ├── app.py                   # Interface principale
│   ├── utils/                   # Fonctions utilitaires
│   ├── models/                  # Gestion des embeddings et LLM
│   └── data/                    # Fichiers PDF, Q&A et index vectoriels
│
├── docs/                        # Documentation Sphinx
│   └── index.html
│
├── requirements.txt             # Dépendances Python
├── README.md                    # Ce fichier
└── LICENSE                      # Licence du projet
```

---

## 💡 Utilisation

### 🔧 Installation

```bash
git clone https://github.com/<votre-utilisateur>/ChatbotPulseLife.git
cd ChatbotPulseLife-main
pip install -r requirements.txt
```

### ▶️ Lancement du Chatbot

```bash
streamlit run app/app.py
```

> Une fois lancé, ouvrez le navigateur à [http://localhost:8501](http://localhost:8501)

---

## 👥 Public Cible

- 🧍‍♂️ Personnes souhaitant surveiller ou améliorer leur santé cardiaque  
- 🩺 Professionnels de santé cherchant un outil d’accompagnement  
- 🎓 Étudiants et chercheurs en IA appliquée à la santé  

---

## 📈 Résultats & Impacts

✅ Réduction du temps de recherche d’information médicale  
✅ Amélioration de la compréhension des risques cardiovasculaires  
✅ Accessibilité à un outil d’assistance intelligent et gratuit  

---

## 🧩 Équipe du Projet

| Nom | Rôle | Contact |
|-----|------|----------|
| **Masrour Tawfik** | Encadrant | [LinkedIn](https://www.linkedin.com/in/tawfik-masrour-43163b85/) |
| **Alae Boutarhat** | Développeuse IA | — |
| **Amina Ismaili** | Développeuse IA & Data Scientist | [LinkedIn](https://www.linkedin.com/in/amina-ismaili-8a0420272/) |

---

## 🏁 Conclusion

Grâce à l’intégration de la **RAG**, des **modèles Mistral et MXBAI**, et d’une **interface Streamlit conviviale**, le **Chatbot des Maladies Cardiaques** constitue un outil performant et éducatif, capable de **répondre efficacement aux besoins de sensibilisation et d’accompagnement** dans le domaine de la santé.

---

## 📜 Licence

Ce projet est distribué sous la licence **MIT** – consultez le fichier `LICENSE` pour plus de détails.
