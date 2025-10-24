
import os
import pdfplumber
from langchain_chroma import Chroma  # Mise à jour de l'import Chroma
from langchain_ollama import OllamaEmbeddings  # Mise à jour de l'import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter # ajjj
pdf_directory = "C:/Users/Administrateur/Desktop/finaldata"

def read_pdf(file_path):
    """Lit un fichier PDF et retourne son contenu sous forme de texte."""
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page_num, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"  # Ajout d'une nouvelle ligne pour séparer les pages
                    print(f"Page {page_num + 1}/{len(pdf.pages)} extraite avec succès.")
                except Exception as e:
                    print(f"Erreur lors de l'extraction de la page {page_num + 1} dans {file_path}: {e}")
            return text
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier PDF {file_path}: {e}")
        return ""  # Retourne un texte vide si une erreur survient

def load_documents_from_directory(directory_path):
    """Charge les documents PDF depuis un répertoire."""
    files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".pdf")]
    documents = []
    for file in files:
        print(f"Traitement du fichier : {file}")
        content = read_pdf(file)
        if content.strip():  # Vérifie si le contenu n'est pas vide
            documents.append(Document(page_content=content))
        else:
            print(f"Aucun contenu extrait du fichier {file}.")
    return documents

def load_all_documents():
    """Charge tous les documents du répertoire."""
    return load_documents_from_directory(pdf_directory)

def ingest_into_vector_store(combined_texts):
    
    # Split text into chunks for vectorization
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=2000,
        chunk_overlap=200,
        separator=".",  # Utilisez le point comme séparateur principal
        keep_separator=False  # Respectez strictement la taille limite
    )
    # Split the documents into chunks
    doc_splits = text_splitter.split_documents(
        [Document(page_content=text.replace(". ", ".\n")) for text in combined_texts]
    )

    # Vérification de la taille de chaque chunk avant de les ajouter au vecteur store
    for chunk in doc_splits:
        token_count = len(chunk.page_content.split())  # Compter les tokens en fonction des espaces
        print(f"Chunk size (tokens): {token_count}")
        if token_count > 2000:
            print("Warning: Chunk size exceeds 2000 tokens!")

    # Initialize the Chroma vector store with a specific collection name
    db = Chroma(
        persist_directory="C:/Users/Administrateur/Desktop/finalbv",
        embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
        collection_name="rag-chroma"
    )

    # Add documents to Chroma (no need for db.persist() anymore)
    db.add_documents(doc_splits)  

    print("Data has been ingested into vector database.")

def initialize_vector_store():
    """Initialize the Chroma vector store for retrieval."""
    db = Chroma(
        persist_directory="C:/Users/Administrateur/Desktop/finalbv",
        embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
        collection_name="rag-chroma"
    )
    return db

def main():
    """Fonction principale qui charge et ingère les documents."""
    all_documents = load_all_documents()
    if all_documents:
        combined_texts = [doc.page_content for doc in all_documents]
        ingest_into_vector_store(combined_texts)
    else:
        print("No data to process.")

# Vérifier si la fonction `main()` a déjà été appelée avant de l'exécuter
if __name__ == "__main__":
    main()

