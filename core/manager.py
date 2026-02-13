import os
import json
import hashlib

class SentinelManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        
        # Extraemos rutas del config
        self.vault_base = self.config.get("vault_path", "./SentinelVault")
        self.project_path = self.config.get("active_project", {}).get("path", "./experiments/poc_01_initialization/mock_project")
        self.project_name = self.config.get("active_project", {}).get("name", "Unnamed_Project")

    def _load_config(self):
        """Lee el archivo config.json de forma segura"""
        if not os.path.exists(self.config_path):
            # Creamos un config básico si no existe
            default_config = {
                "vault_path": "./SentinelVault",
                "active_project": {
                    "path": "./experiments/poc_01_initialization/mock_project",
                    "name": "POC_01_Chat_Test"
                }
            }
            with open(self.config_path, "w") as f:
                json.dump(default_config, f, indent=4)
            return default_config
        
        with open(self.config_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Error: {self.config_path} está vacío o mal formado.")
                return {}

    def get_vault_for_active_project(self):
        """Genera la ruta de la Vault (Bóveda) única para el proyecto"""
        # Usamos ruta absoluta para el hash para que sea único
        abs_project_path = os.path.abspath(self.project_path)
        project_id = hashlib.md5(abs_project_path.encode()).hexdigest()[:8]
        
        vault_path = os.path.join(self.vault_base, f"{self.project_name}_{project_id}")
        return os.path.abspath(vault_path)

    def setup_vault_folders(self, vault_path):
        """Crea la estructura cognitiva dentro de la Vault"""
        structure = [
            "identity", "project", "state", "memory/decisions"
        ]
        for folder in structure:
            os.makedirs(os.path.join(vault_path, folder), exist_ok=True)