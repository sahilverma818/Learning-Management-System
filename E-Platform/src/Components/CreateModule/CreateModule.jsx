import { useState } from "react";
import "./CreateModule.css";

export default function CreateModule({ isOpen, onClose }) {
  const [moduleTitle, setModuleTitle] = useState("");
  const [moduleDescription, setModuleDescription] = useState("");

  const handleSave = () => {
    if (moduleTitle.trim() === "" || moduleDescription.trim() === "") return;
    setModuleTitle("");
    setModuleDescription("");
  };

  return (
    <div className={`popup-container ${isOpen ? 'show' : ''}`}>
      <div className="popup-content">
        <h2>Create Module</h2>
        <input
          type="text"
          placeholder="Module Title"
          value={moduleTitle}
          onChange={(e) => setModuleTitle(e.target.value)}
        />
        <textarea
          placeholder="Module Description"
          value={moduleDescription}
          onChange={(e) => setModuleDescription(e.target.value)}
        />
        <div className="popup-actions">
          <button className="cancel" onClick={onClose}>Cancel</button>
          <button className="save" onClick={handleSave}>Save</button>
        </div>
      </div>
    </div>
  );
}
