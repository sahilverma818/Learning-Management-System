import { Routes, Route } from "react-router-dom"
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import Navbar from "./Components/Navbar/Navbar"
import Footer from "./Components/Footer/Footer"
import Home from "./pages/Home/Home"
import CourseDetails from "./pages/Courses/CourseDetails"
import Login from "./Components/Login/Login"
import SignUp from "./Components/SignUp/signUp"

function App() {
  
  return (
    <>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/course/:id' element={<CourseDetails />}/>
        <Route path='/login' element={<Login />} />
        <Route path="/register" element={ <SignUp />}/>
      </Routes>
      <Footer/>
      <ToastContainer />
    </>
  )
}

export default App
