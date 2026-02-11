import os
import json
import hashlib

class SentinelManager:
    def __init__(self, vault_path=None):
        # Si no se define, usamos una carpeta por defecto en el usuario
        if vault_path is None:
            self.vault_path = os.path.join(os.path.expanduser("~"), ".sentinel_vault")
        else:
            self.vault_path = vault_path
        
        os.makedirs(self.vault_path, exist_ok=True)

    def get_project_id(self, project_path):
        """Genera un ID único basado en la ruta del proyecto para evitar colisiones"""
        return hashlib.md5(project_path.encode()).hexdigest()[:10]

    def get_memory_path(self, project_path):
        """Retorna la ruta de la memoria de Sentinel para un proyecto específico"""
        project_name = os.path.basename(project_path)
        project_id = self.get_project_id(project_path)
        
        # Ruta: Vault / NombreProyecto_ID
        memory_path = os.path.join(self.vault_path, f"{project_name}_{project_id}")
        self._initialize_structure(memory_path)
        return memory_path

    def _initialize_structure(self, memory_path):
        """Crea la jerarquía .md dentro de la Vault, no en el proyecto"""
        folders = [
            "identity", "project", "runtime", "state", "embeddings",
            "memory/structure/files", "memory/logic", "memory/decisions"
        ]
        for folder in folders:
            os.makedirs(os.path.join(memory_path, folder), exist_ok=True)

# --- PRUEBA DE CONCEPTO ---
if __name__ == "__main__":
    # Supongamos que el usuario quiere trabajar en este proyecto
    my_code_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    
    manager = SentinelManager() # Usará la carpeta del sistema por defecto
    memory_dir = manager.get_memory_path(my_code_path)
    
    print(f"📂 Código del usuario: {my_code_path}")
    print(f"🧠 Memoria de Sentinel: {memory_dir}")