import './App.css';
import "bootstrap/dist/css/bootstrap.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Konyvek from './Konyvek';
import EgyKonyv from './egyKonyv';
import UjKonyv from './ujKonyv';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Konyvek />} />
        <Route path='/egyKonyv/:id' element={<EgyKonyv />} />
        <Route path='/ujKonyv' element={<UjKonyv />} />
      </Routes>
    </Router>
  );
}

export default App;
