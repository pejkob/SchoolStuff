import React, { useEffect, useState } from 'react';
import { useParams, NavLink } from 'react-router-dom';
import axios from 'axios';

function EgyFilm() {
    const { id } = useParams(); 
    const [egyFilm, setEgyFilm] = useState({});
    const [editedFilm, setEditedFilm] = useState({});
    const url = "https://localhost:7017/Film";

    const handleEdit = () => {
        editedFilm.id=id;
        axios.put(url + `/${id}`, editedFilm)
            .then(response => {
                window.location.href = '/';
   
               
            })
            .catch(error =>console.log(editedFilm));
    };

    const fetchFilmDetails = () => {
        const url = `https://localhost:7017/Film/${id}`; 
        axios.get(url)
            .then(response => setEgyFilm(response.data))
            .catch(error => console.error('Hiba a lekérdezés során:', error));
    };

    useEffect(() => {
        fetchFilmDetails();
    }, [id]); 

    const handleDelete = () => {
        axios.delete(url + `/${id}`)
          .then(response => {
              window.location.href = '/';
          })
          .catch(error => console.error('Error deleting book:', error));
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditedFilm({ ...editedFilm, [name]: value });
    };

    return (
        <>
            <NavLink className={'btn btn-secondary'} to={'/'}>Vissza</NavLink>

            <div className='card' style={{ display: 'inline-block', margin: '10px', width: '100%', maxHeight: '800px' }}>
                <div className='card-body'>
                    <p className='card-text text-center'>Film neve: {egyFilm.nev}</p>
                    <p className='card-title text-center'><strong>Kiadás éve: {egyFilm.kiadasEve}</strong></p>
                    <p className='card-text text-center'>Film értékelése: {egyFilm.ertekeles}</p>
                    <img src={"/"+egyFilm.kepneve} alt={egyFilm.nev} width={250} className='mx-auto d-block' />
                    <div className='text-center'>
                        <div className='delete' style={{ display: 'inline-block' }} onClick={handleDelete}>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-trash3" viewBox="0 0 16 16">
                                <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.
                                5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5"/>
                                </svg>
                            </div>
                            <div className='modify' style={{ display: 'inline-block' }} >
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-pencil" viewBox="0 0 16 16">
                                <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"/>
                            </svg>
                        </div>
                        </div>
                    </div>
                </div>
    

                    <>
                        <input className='form-control' type='text' placeholder='Könyv neve' name='nev' value={editedFilm.nev || ''} onChange={handleInputChange} />
                        <input className='form-control' type='number' placeholder='Kiadás éve' name='kiadasEve' value={editedFilm.kiadasEve || ''} onChange={handleInputChange} />
                        <input className='form-control' type='number' placeholder='Értékelés' name='ertekeles' value={editedFilm.ertekeles || ''} onChange={handleInputChange} />
                        <input className='form-control' type='text' placeholder='Kép neve' name='kepneve' value={editedFilm.kepneve || ''} onChange={handleInputChange} />
                        <button className='btn btn-warning' onClick={handleEdit}>Módosítás</button>
                    </>
                   
            </>
        );
    }
    
    export default EgyFilm;
    