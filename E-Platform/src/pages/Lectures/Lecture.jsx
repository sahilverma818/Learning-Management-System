import React from "react"
import VideoComponent from "../../Components/VideoComponent/VideoComponent"
import VideoSidebar from "../../Components/VideoSidebar/VideoSidebar"
import "./Lectures.css"

const Lectures = () => {
    return (
      <div>
        <div className="main-content">
          <div className="video-component">
            <VideoComponent />
          </div>
          <div className="video-sidebar">
            <VideoSidebar />
          </div>
        </div>
      </div>
    );
  };
  
  export default Lectures;