import './App.css';
import "bootstrap/dist/css/bootstrap.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Filmek from './Filmek';
import EgyFilm from './egyFilm';
import UjFilm from './ujFilm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Filmek />} />
        <Route path='/egyFilm/:id' element={<EgyFilm />} />
        <Route path='/ujFilm' element={<UjFilm />} />
      </Routes>
    </Router>
  );
}

export default App;
