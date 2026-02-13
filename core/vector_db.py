import chromadb
import os

class SentinelVectorDB:
    def __init__(self, vault_path):
        # Base de datos persistente en la Vault
        self.client = chromadb.PersistentClient(path=os.path.join(vault_path, "embeddings"))
        self.collection = self.client.get_or_create_collection(name="code_logic")

    def index_file(self, file_path, content, metadata):
        """Guarda el contenido de un archivo en la memoria vectorial"""
        self.collection.upsert(
            documents=[content],
            metadatas=[metadata],
            ids=[file_path] # Usamos la ruta como ID único
        )

    def search(self, query, n_results=3):
        """Busca fragmentos de código relevantes"""
        return self.collection.query(query_texts=[query], n_results=n_results)