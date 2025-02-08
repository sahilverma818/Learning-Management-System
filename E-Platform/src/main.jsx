import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

import 'bootstrap/dist/css/bootstrap.min.css';

// export browser router
import { BrowserRouter as Router } from 'react-router-dom'
import CourseContextProvider from './Components/CourseContext/CourseContext.jsx'

createRoot(document.getElementById('root')).render(
      <Router>
        <StrictMode>
          <App />
        </StrictMode>
      </Router>
)
