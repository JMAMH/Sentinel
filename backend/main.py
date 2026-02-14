import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importamos el router que acabamos de corregir
from app.api.router import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Sentinel Backend",
        description="Motor proactivo de IA con memoria persistente",
        version="0.1.0"
    )

    # Configuración de CORS para comunicación con el frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Inyectamos las rutas de la API bajo el prefijo /api
    app.include_router(api_router, prefix="/api")

    @app.get("/")
    async def root():
        return {"message": "Sentinel Core is Running", "status": "active"}

    return app

app = create_app()

if __name__ == "__main__":
    # Ejecutamos con reload=True para que se reinicie al detectar cambios
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)