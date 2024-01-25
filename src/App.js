import "./App.css"
import Header from './Component/common/header/Header'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import About from './Component/about/About'
import CourseHome from './Component/allcourses/CourseHome'
import Team from './Component/team/Team'
import Pricing from './Component/pricing/Pricing'
import Blog from './Component/blog/Blog'
import Contact from './Component/contact/contact'
import Footer from './Component/common/footer/Footer'
import Home from './Component/home/Home'
function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
        <Route exact path='/' component={Home} />
          <Route exact path='/about' component={About} />
          <Route exact path='/courses' component={CourseHome} />
          <Route exact path='/team' component={Team} />
          <Route exact path='/pricing' component={Pricing} />
          <Route exact path='/journal' component={Blog} />
          <Route exact path='/contact' component={Contact} />
        </Routes>
         
        <Footer />
      </Router>
    </>
  )
}

export default App
