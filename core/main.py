import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import chromadb # Importamos Chroma

load_dotenv()

class Sentinel:
    def __init__(self, project_path):
        self.project_path = project_path
        self.ai_dir = os.path.join(project_path, ".ai")
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # 1. Inicializar base de datos vectorial local (Plug & Play)
        self.chroma_client = chromadb.PersistentClient(path=os.path.join(self.ai_dir, "embeddings"))
        self.collection = self.chroma_client.get_or_create_collection(name="codebase_index")

        # 2. Crear estructura de carpetas .ai/
        self._initialize_memory_structure()

    def _initialize_memory_structure(self):
        """Crea la jerarquía de memoria definida en la visión"""
        folders = [
            "identity", "project", "runtime", "git", "state",
            "memory/structure/files", "memory/logic", "memory/decisions", "memory/history"
        ]
        for folder in folders:
            os.makedirs(os.path.join(self.ai_dir, folder), exist_ok=True)
        
        # Crear archivos iniciales si no existen
        self._touch_file("identity/sentinel.md", "# Sentinel Identity\nRole: Proactive AI Agent")
        self._touch_file("state/todo.md", "# Current Tasks\n- [ ] Complete memory initialization")

    def _touch_file(self, relative_path, content=""):
        path = os.path.join(self.ai_dir, relative_path)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    def index_project(self):
        """
        Escanea el proyecto y guarda fragmentos en ChromaDB.
        Esto permitirá a la IA buscar archivos por significado.
        """
        print("🔍 Sentinel: Indexando archivos en la base de datos vectorial...")
        # Aquí iría la lógica para leer archivos y guardarlos en self.collection
        # Por ahora lo dejamos como hito para la siguiente iteración.
        pass

    def run_query(self, user_input):
        # Aquí Sentinel consultará primero ChromaDB para saber qué leer
        # Luego leerá los .md de .ai/ para tener contexto
        # Y finalmente responderá.
        system_instruction = "Eres Sentinel. Consulta .ai/ antes de responder."
        
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input,
            config=types.GenerateContentConfig(system_instruction=system_instruction)
        )
        return response.text

if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sentinel = Sentinel(base_path)
    print("🛡️ Sentinel activo y con memoria estructurada.")