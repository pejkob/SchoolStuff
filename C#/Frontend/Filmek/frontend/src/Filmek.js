import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';

function Filmek() {
  const [filmList, setFilmList] = useState([]);

 

  const url = 'https://localhost:7017/Film';
  useEffect(() => {
    axios.get(url)
      .then(response => setFilmList(response.data))
      .catch(error => console.error('Hiba a lekérdezés során:', error));
  }, []);

  const films = filmList.map(item => (
  
    <NavLink to={'/egyFilm/'+item.id}>

    
    <div className='card' style={{ display: 'inline-block', margin: '10px', width:'30%',maxHeight:'500px',minHeight:'499px' }}>
      <div className='card-body'>
        <p className='card-text text-center'>Film neve: {item.nev}</p>
        <p className='card-title text-center'><strong>Kiadás éve: {item.kiadasEve}</strong>  </p>
        <p className='card-text text-center'>Film értékelése: {item.ertekeles}</p>
        <img src={"/"+item.kepneve} alt={item.nev} width={250} className='mx-auto d-block' />
        </div>
      </div>
      </NavLink>

  ));

  return (
    <div className='container'>
      <NavLink className={'btn btn-secondary'} to={'/ujFilm'}>Új Film</NavLink>
      <div className='row'>
        <div className='col-12'>
          {films}
        </div>
      </div>
    </div>
  );
}

export default Filmek;
