import os
import json
import hashlib

class SentinelManager:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        
        self.vault_base = self.config.get("vault_path", "./SentinelVault")
        self.project_path = self.config.get("active_project", {}).get("path", "")
        self.project_name = self.config.get("active_project", {}).get("name", "Unknown")
        # Nuevo: Extraer el modelo
        self.model_id = self.config.get("ai", {}).get("model", "gemini-1.5-flash")

    def _load_config(self):
        if not os.path.exists(self.config_path):
            return {}
        with open(self.config_path, "r") as f:
            try:
                return json.load(f)
            except:
                return {}

    def get_vault_for_active_project(self):
        abs_path = os.path.abspath(self.project_path)
        p_id = hashlib.md5(abs_path.encode()).hexdigest()[:8]
        return os.path.abspath(os.path.join(self.vault_base, f"{self.project_name}_{p_id}"))

    def setup_vault_folders(self, vault_path):
        structure = [
            "identity", "project", "state", 
            "memory/structure/files", "memory/logic"
        ]
        for folder in structure:
            os.makedirs(os.path.join(vault_path, folder), exist_ok=True)