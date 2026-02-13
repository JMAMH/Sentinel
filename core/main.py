import os
import json
from google import genai
from google.genai import types
from manager import SentinelManager
from vector_db import SentinelVectorDB
from dotenv import load_dotenv

load_dotenv()

class SentinelCore:
    def __init__(self):
        self.manager = SentinelManager()
        self.vault_path = self.manager.get_vault_for_active_project()
        self.manager.setup_vault_folders(self.vault_path)
        
        # Ojos: IA | Memoria: VectorDB
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.vdb = SentinelVectorDB(self.vault_path)
        self.model = self.manager.model_id

    def deep_audit(self):
        """
        POC 03: Lee CONTENIDO de archivos, resume lógica e indexa en vectores.
        """
        print(f"🧠 Sentinel: Iniciando análisis profundo de {self.manager.project_path}...")
        
        ignore_ext = ['.png', '.jpg', '.ico', '.pyc'] # Evitar binarios por ahora
        
        for root, dirs, files in os.walk(self.manager.project_path):
            for file in files:
                if any(file.endswith(ext) for ext in ignore_ext): continue
                
                rel_path = os.path.relpath(os.path.join(root, file), self.manager.project_path)
                full_path = os.path.join(root, file)
                
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # 1. Indexar en ChromaDB para búsqueda futura
                self.vdb.index_file(rel_path, content, {"path": rel_path})

                # 2. Pedir a la IA un resumen técnico de este archivo específico
                print(f"📄 Analizando lógica de: {rel_path}...")
                self._summarize_file(rel_path, content)

        return "🚀 Análisis profundo completado. La memoria lógica ha sido poblada."

    def _summarize_file(self, file_path, content):
        instruction = f"""
        Eres Sentinel. Analiza el código de '{file_path}' y resume su propósito.
        Identifica: funciones principales, dependencias y lógica clave.
        Responde en formato Markdown técnico.
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=f"Código de {file_path}:\n\n{content}",
                config=types.GenerateContentConfig(system_instruction=instruction)
            )
            
            # Guardamos el resumen en Vault/memory/structure/files/nombre_archivo.md
            summary_path = os.path.join("memory/structure/files", f"{file_path}.md")
            self._write_to_vault(summary_path, response.text)
        except Exception as e:
            print(f"⚠️ Error analizando {file_path}: {e}")

    def _write_to_vault(self, rel_path, content):
        full_path = os.path.join(self.vault_path, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    sentinel = SentinelCore()
    print(sentinel.deep_audit())