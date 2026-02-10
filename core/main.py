import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no está configurado")

# 1. Configuración (Usa variables de entorno en el futuro)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class SentinelCore:
    def __init__(self, project_path):
        self.project_path = project_path
        self.ai_folder = os.path.join(project_path, ".ai")
        
        if not os.path.exists(self.ai_folder):
            os.makedirs(self.ai_folder)

    def get_project_context(self):
        # Una forma simple de listar archivos para darle contexto a la IA
        files = [f for f in os.listdir(self.project_path) if os.path.isfile(f)]
        return f"Archivos actuales en el proyecto: {', '.join(files)}"

    def ask_sentinel(self, user_query):
        context = self.get_project_context()
        
        # El "System Prompt" (instrucciones para la IA)
        prompt = f"""
        Eres Sentinel, un agente de IA proactivo.
        Contexto del proyecto: {context}
        Instrucción del usuario: {user_query}
        
        Tu objetivo es proponer un plan de acción basado en el estado actual.
        """
        
        response = model.generate_content(prompt)
        return response.text

# --- PRUEBA DEL MOTOR ---
if __name__ == "__main__":
    # Inicializa Sentinel en la carpeta actual
    bot = SentinelCore(os.getcwd())
    
    print("Sentinel: Analizando proyecto...")
    respuesta = bot.ask_sentinel("¿Qué puedes decirme de este proyecto y qué archivos ves?")
    print(f"\nSentinel responde:\n{respuesta}")