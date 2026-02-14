from fastapi import APIRouter, Query
import os
from app.services.manager import ProjectManager

# Definimos el router una sola vez de forma correcta
router = APIRouter()
manager = ProjectManager()

@router.get("/project/status")
async def project_status():
    """Devuelve el proyecto activo actual"""
    active = manager.get_active_project()
    return {
        "active_project": active,
        "is_configured": active is not None
    }

@router.post("/project/init")
async def init_project(path: str):
    """Inicializa la estructura .ai/ en la carpeta del proyecto"""
    try:
        ai_folder = manager.setup_project_vault(path)
        return {"status": "success", "path": ai_folder}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/project/files")
async def get_files(path: str = Query(...)):
    """Escanea la carpeta del proyecto y devuelve una lista de archivos"""
    try:
        files_list = []
        # Ignoramos carpetas pesadas o irrelevantes para no saturar
        ignore_list = {'.git', 'node_modules', '__pycache__', '.ai', 'dist', 'venv'}
        
        for root, dirs, files in os.walk(path):
            # Filtrar carpetas ignoradas
            dirs[:] = [d for d in dirs if d not in ignore_list]
            
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), path)
                files_list.append({
                    "name": file,
                    "path": rel_path,
                    "type": "file"
                })
        return {"files": files_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}