import { useState, useEffect } from "react";
import { Sidebar } from "./components/Sidebar";
import { open } from "@tauri-apps/plugin-dialog";
import axios from "axios";
import "./App.css";

function App() {
  const [view, setView] = useState<"list" | "workspace">("list");
  const [activeProject, setActiveProject] = useState<string | null>(null);
  const [files, setFiles] = useState<{name: string, path: string}[]>([]);

  useEffect(() => {
  if (activeProject && view === "workspace") {
    const fetchFiles = async () => {
      const res = await axios.get(`http://127.0.0.1:8000/api/project/files?path=${encodeURIComponent(activeProject)}`);
      if (res.data.files) setFiles(res.data.files);
    };
    fetchFiles();
  }
}, [activeProject, view]);

  const handleNewProject = async () => {
    try {
      const selected = await open({
        directory: true,
        multiple: false,
        title: "Seleccionar Carpeta del Proyecto"
      });

      if (selected) {
        // En Windows el path viene como string, en Mac/Linux como array. Forzamos string.
        const path = Array.isArray(selected) ? selected[0] : selected;
        await axios.post(`http://127.0.0.1:8000/api/project/init?path=${encodeURIComponent(path)}`);
        setActiveProject(path);
        setView("workspace");
      }
    } catch (err) {
      alert("Error: ¿Está el backend encendido?");
      console.error(err);
    }
  };

  return (
    <div className="app-layout">
      {/* Solo mostramos el sidebar si estamos en la lista de proyectos */}
      {view === "list" && <Sidebar onNewProject={handleNewProject} />}
      
      <main className="content">
        {view === "list" ? (
          <div className="projects-list">
            <header style={{padding: '30px'}}>
              <h1>Recent Projects</h1>
            </header>
            <div className="projects-grid">
              <div className="project-card" onClick={() => setView("workspace")}>
                <div className="card-image"></div>
                <div className="card-info">
                  <h3>E-commerce Refactor</h3>
                  <p>Haga clic para entrar al espacio de trabajo</p>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="workspace-container">
            {/* BARRA SUPERIOR (Botones de acción) */}
            <header className="workspace-header">
              <div className="project-title">📁 {activeProject?.split('\\').pop() || "Proyecto"}</div>
              <div className="actions">
                <button className="action-btn orange">▶ Run</button>
                <button className="action-btn">Scan</button>
                <button className="action-btn" onClick={() => setView("list")}>✕ Close</button>
              </div>
            </header>
            
            {/* CUERPO DEL IDE (3 COLUMNAS) */}
            <div className="ide-body">
              <div className="explorer-column">
                <div className="column-label">EXPLORER</div>
                <div className="file-list">
                  {files.map((file, idx) => (
                    <div key={idx} className="file-item" title={file.path}>
                      📄 {file.name}
                    </div>
                  ))}
                  {files.length === 0 && <div className="empty-msg">Carpeta vacía</div>}
                </div>
              </div>
              
              <div className="editor-column">
                <div className="editor-placeholder">
                  {/* Aquí irá el editor de código */}
                  <code style={{color: '#4f4f4f'}}>// Selecciona un archivo para editar</code>
                </div>
              </div>
              
              <div className="chat-column">
                <div className="column-label">SENTINEL CHAT</div>
                <div className="chat-messages"></div>
                <div className="chat-input-area">
                  <input type="text" placeholder="Pregunta a Sentinel..." />
                </div>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;