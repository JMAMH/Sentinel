from pathlib import Path
import datetime

class MemoryService:
    def __init__(self, project_path: str):
        self.ai_path = Path(project_path) / ".ai"

    def write_decision(self, title: str, content: str):
        """Registra una decisión técnica en memory/decisions/"""
        decision_path = self.ai_path / "memory" / "decisions"
        decision_path.mkdir(parents=True, exist_ok=True)
        
        filename = f"{datetime.date.today()}_{title.lower().replace(' ', '_')}.md"
        with open(decision_path / filename, "w", encoding="utf-8") as f:
            f.write(f"# Decision: {title}\n\n{content}")

    def update_state(self, key: str, value: str):
        """Actualiza el estado inmediato en .ai/state/"""
        state_file = self.ai_path / "state" / f"{key}.md"
        with open(state_file, "w", encoding="utf-8") as f:
            f.write(value)

    def get_context_for_llm(self) -> str:
        """Lee la identidad y visión para darle contexto al Agente"""
        # Por ahora simplificado, luego usaremos RAG o lectura de MDs
        return "Contexto del proyecto extraído de .ai/"