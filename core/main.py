import os
import json
from google import genai
from google.genai import types
from manager import SentinelManager
from dotenv import load_dotenv

load_dotenv()

class SentinelCore:
    def __init__(self):
        # 1. Inicializar el Manager (lee config.json)
        self.manager = SentinelManager()
        
        # 2. Obtener y preparar la Vault
        self.vault_path = self.manager.get_vault_for_active_project()
        self.manager.setup_vault_folders(self.vault_path)
        
        # 3. Configurar Cliente de IA
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ No se encontró GEMINI_API_KEY en el archivo .env")
            
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash"

    def chat_and_initialize_memory(self, user_input):
        """
        POC 01: Chat inicial para definir visión e identidad.
        Escribe en la Vault, no en el proyecto del usuario.
        """
        print(f"\n🧠 Sentinel procesando idea...")

        instruction = """
        Eres Sentinel, un agente de IA con memoria estructurada.
        Tu objetivo hoy es INICIALIZAR los cimientos de este proyecto basándote en lo que diga el usuario.
        
        Debes generar:
        1. 'project/vision.md': Un resumen del propósito y metas.
        2. 'identity/sentinel.md': Cómo vas a actuar y tus reglas de oro aquí.
        
        RESPUESTA: Debes responder EXCLUSIVAMENTE en formato JSON con estas llaves:
        {
          "vision": "contenido para vision.md",
          "identity": "contenido para sentinel.md",
          "chat_response": "mensaje amigable para el usuario resumiendo lo que entendiste"
        }
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=user_input,
                config=types.GenerateContentConfig(
                    system_instruction=instruction,
                    response_mime_type="application/json"
                )
            )

            res = json.loads(response.text)
            
            # Guardar archivos en la Vault
            self._write_to_vault("project/vision.md", res.get("vision", ""))
            self._write_to_vault("identity/sentinel.md", res.get("identity", ""))
            
            return res.get("chat_response", "Memoria actualizada.")

        except Exception as e:
            return f"❌ Error en la IA: {str(e)}"

    def _write_to_vault(self, rel_path, content):
        if not content: return
        full_path = os.path.join(self.vault_path, rel_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📝 Vault actualizada: {rel_path}")

if __name__ == "__main__":
    print("--- 🛡️ SENTINEL POC 01: INICIALIZACIÓN COGNITIVA ---")
    
    try:
        sentinel = SentinelCore()
        print(f"📍 Proyecto: {sentinel.manager.project_path}")
        print(f"🔒 Vault: {sentinel.vault_path}\n")
        
        user_msg = input("Humano (describe tu idea): ")
        
        resultado = sentinel.chat_and_initialize_memory(user_msg)
        print(f"\n🤖 Sentinel: {resultado}")
        print("\n✅ Prueba finalizada. Revisa la carpeta SentinelVault.")
        
    except Exception as e:
        print(f"💥 Error fatal: {e}")