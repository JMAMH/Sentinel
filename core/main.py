import os
import json
from google import genai
from google.genai import types
from manager import SentinelManager
from dotenv import load_dotenv

load_dotenv()

class SentinelCore:
    def __init__(self):
        self.manager = SentinelManager()
        self.vault_path = self.manager.get_vault_for_active_project()
        self.manager.setup_vault_folders(self.vault_path)
        
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = self.manager.model_id
        print(f"🤖 Sentinel inicializado con el modelo: {self.model}")

    def perform_first_audit(self):
        """
        POC 02: Mira el proyecto real y documenta la estructura en la Vault.
        """
        print(f"🔍 Escaneando archivos en: {self.manager.project_path}...")
        
        # 1. Escaneo físico de archivos
        files_list = []
        for root, dirs, files in os.walk(self.manager.project_path):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), self.manager.project_path)
                files_list.append(rel_path)

        # 2. Instrucción para la IA (especificando formato Markdown)
        instruction = f"""
        Eres Sentinel. Estás realizando una auditoría técnica de un repositorio.
        Archivos detectados: {files_list}
        
        Tu tarea es generar documentación técnica para la memoria del agente.
        
        RESPUESTA JSON (Todo el contenido debe ser STRING en formato Markdown):
        {{
          "folders_summary": "# Estructura de Archivos\\n\\n(Lista de archivos con su descripción técnica)",
          "tech_stack": "# Stack Tecnológico\\n\\n(Lista de tecnologías y lenguajes detectados)",
          "chat_response": "(Resumen amigable para el usuario)"
        }}
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents="Analiza los archivos y genera la documentación técnica.",
                config=types.GenerateContentConfig(
                    system_instruction=instruction,
                    response_mime_type="application/json"
                )
            )

            res = json.loads(response.text)
            
            # 3. Guardar descubrimientos con el nuevo manejador de tipos
            self._write_to_vault("memory/structure/folders.md", res.get("folders_summary", ""))
            self._write_to_vault("project/stack.md", res.get("tech_stack", ""))
            
            return res.get("chat_response", "Auditoría finalizada.")

        except Exception as e:
            return f"❌ Error: {str(e)}"

    def _write_to_vault(self, rel_path, content):
        """Guarda contenido asegurándose de que sea string"""
        if not content: return
        
        # SI LA IA ENVÍA UNA LISTA, LA CONVERTIMOS A TEXTO
        if isinstance(content, list):
            content = "\n".join([f"- {item}" for item in content])
        elif isinstance(content, dict):
            content = json.dumps(content, indent=2)

        full_path = os.path.join(self.vault_path, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(str(content)) # Aseguramos string por si acaso
        print(f"📝 Vault actualizada: {rel_path}")

if __name__ == "__main__":
    sentinel = SentinelCore()
    print(f"\n🤖 Sentinel: {sentinel.perform_first_audit()}")