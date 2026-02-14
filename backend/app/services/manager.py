import os
import json
import hashlib
from pathlib import Path

class ProjectManager:
    def __init__(self, config_path: str = "../config.json"):
        self.config_path = Path(config_path).resolve()
        self.config = self._load_config()

    def _load_config(self):
        if not self.config_path.exists():
            # Configuración por defecto si no existe
            default_config = {
                "vault_path": str(Path.home() / ".sentinel_vault"),
                "active_project": None,
                "llm_model": "gemini-2.0-flash"
            }
            with open(self.config_path, "w") as f:
                json.dump(default_config, f, indent=4)
            return default_config
        
        with open(self.config_path, "r") as f:
            return json.load(f)

    def get_project_id(self, project_path: str) -> str:
        """Genera un ID único basado en la ruta del proyecto"""
        abs_path = str(Path(project_path).resolve())
        return hashlib.md5(abs_path.encode()).hexdigest()[:10]

    def setup_project_vault(self, project_path: str):
        """Prepara la carpeta .ai/ dentro del proyecto (Filosofía Sentinel)"""
        ai_path = Path(project_path) / ".ai"
        
        # Subcarpetas obligatorias según nuestra arquitectura cognitiva
        subfolders = [
            "identity", "project", "memory/structure", 
            "memory/logic", "runtime", "state"
        ]
        
        for folder in subfolders:
            (ai_path / folder).mkdir(parents=True, exist_ok=True)
            
        return str(ai_path)

    def get_active_project(self):
        return self.config.get("active_project")