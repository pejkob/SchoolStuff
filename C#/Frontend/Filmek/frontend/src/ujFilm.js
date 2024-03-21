import axios from 'axios';
import React, { useState } from 'react';
import { NavLink, Navigate } from 'react-router-dom';
function UjFilm() {
    const [filmData, setfilmData] = useState({
        nev: '',
        kiadasEve: '',
        ertekeles: '',
        kepneve: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setfilmData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const newfilmSend = () => {
        axios.post("https://localhost:7017/Film", filmData)
            .then(response => {
                console.log('New film added successfully:', response.data);
              
                setfilmData({
                    nev: '',
                    kiadasEve: '',
                    ertekeles: '',
                    kepneve: ''
                });
                <Navigate to="/" replace={true} />
            })
            .catch(error => {
                console.error('Error adding new film:', error);
            });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        newfilmSend();
        
    };

    return (
        <div>
            <NavLink className={'btn btn-sencodary'} to={'/'}>Vissza</NavLink>
            <div className='container'>
                <form onSubmit={handleSubmit}>
                    <input type='text' name='nev' value={filmData.nev} onChange={handleChange} className='form-control' placeholder='Film Neve' />
                    <input type='number' name='kiadasEve' value={filmData.kiadasEve} onChange={handleChange} className='form-control' placeholder='Kiadás éve' />
                    <input type='number' name='ertekeles' value={filmData.ertekeles} onChange={handleChange} className='form-control' placeholder='Értékelés' />
                    <input type='text' name='kepneve' value={filmData.kepneve} onChange={handleChange} className='form-control' placeholder='Kép Neve' />
                    <button type='submit' className='btn btn-success'>Küldés</button>
                </form>
            </div>
        </div>
    );
}

export default UjFilm;
