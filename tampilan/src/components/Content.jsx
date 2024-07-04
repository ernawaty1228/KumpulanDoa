import React, { useEffect, useState } from 'react';
import './Content.css';

function Content() {
  const [doaList, setDoaList] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/doa/')
      .then(response => response.json())
      .then(data => {
        setDoaList(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="container">
      {doaList.length > 0 ? (
        <div>
          {doaList.map(doa => (
            <div key={doa.id} className="card mx-auto mb-3" style={{ maxWidth: '600px' }}>
              <div className="card-body">
                <h5 className="card-title">{doa.judul}</h5>
                <p className="card-text"><strong>Arab:</strong> {doa.arab}</p>
                <p className="card-text"><strong>Arti:</strong> {doa.arti}</p>
                <p className="card-text"><small className="text-muted">Tanggal Dibuat: {new Date(doa.tanggal_dibuat).toLocaleString()}</small></p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Content;