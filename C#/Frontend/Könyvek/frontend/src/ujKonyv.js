import axios from 'axios';
import React, { useState } from 'react';
import { NavLink, Navigate } from 'react-router-dom';
function UjKonyv() {
    const [bookData, setBookData] = useState({
        nev: '',
        kiadasEve: '',
        ertekeles: '',
        kepneve: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setBookData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const newBookSend = () => {
        axios.post("https://localhost:7017/Konyv", bookData)
            .then(response => {
                console.log('New book added successfully:', response.data);
              
                setBookData({
                    nev: '',
                    kiadasEve: '',
                    ertekeles: '',
                    kepneve: ''
                });
                <Navigate to="/" replace={true} />
            })
            .catch(error => {
                console.error('Error adding new book:', error);
            });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        newBookSend();
        
    };

    return (
        <div>
            <NavLink className={'btn btn-sencodary'} to={'/'}>Vissza</NavLink>
            <div className='container'>
                <form onSubmit={handleSubmit}>
                    <input type='text' name='nev' value={bookData.nev} onChange={handleChange} className='form-control' placeholder='Könyv Neve' />
                    <input type='number' name='kiadasEve' value={bookData.kiadasEve} onChange={handleChange} className='form-control' placeholder='Kiadás éve' />
                    <input type='number' name='ertekeles' value={bookData.ertekeles} onChange={handleChange} className='form-control' placeholder='Értékelés' />
                    <input type='text' name='kepneve' value={bookData.kepneve} onChange={handleChange} className='form-control' placeholder='Kép Neve' />
                    <button type='submit' className='btn btn-success'>Küldés</button>
                </form>
            </div>
        </div>
    );
}

export default UjKonyv;
