import './Sidebar.css';

interface SidebarProps {
  onNewProject: () => void;
}

export const Sidebar = ({ onNewProject }: SidebarProps) => {
  return (
    <aside className="sidebar">
      <div className="logo-section">
        <div className="logo-icon">S</div>
        <h2>Sentinel</h2>
      </div>
      
      {/* Ahora este botón llama a la función handleNewProject de App.tsx */}
      <button className="new-project-btn" onClick={onNewProject}>
        New Project
      </button>
      
      <nav className="nav-menu">
        <div className="nav-item">Dashboard</div>
        <div className="nav-item active">Projects</div>
        <div className="nav-item">AI Agents</div>
        <div className="nav-item">Settings</div>
      </nav>
    </aside>
  );
};