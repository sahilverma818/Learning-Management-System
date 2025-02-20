import React from 'react';
import './VideoSidebar.css';

const VideoSidebar = () => {
  const videoDays = [
    "Day 1 - What is Programming and Python?",
    "Day 2 - My Python Success Story",
    "Day 3 - Modules and pip in Python!",
    "Day 4 - Our First Program",
    "Day 5 - Comments, Escape sequence & Print in Python",
    "Day 1 - What is Programming and Python?",
    "Day 2 - My Python Success Story",
    "Day 3 - Modules and pip in Python!",
    "Day 4 - Our First Program",
    "Day 5 - Comments, Escape sequence & Print in Python",
    // ... add more days as needed
  ];

  return (
    <aside className="sidebar">
      <h2>Course Contents</h2>
      <ul>
        {videoDays.map((day, index) => (
          <li key={index}>
            <div className="lecture-card">
              <a href="#">{day}</a>
            </div>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default VideoSidebar;
