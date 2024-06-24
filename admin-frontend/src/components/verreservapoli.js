import jsPDF from 'jspdf';
import React, { useEffect, useState } from 'react';


const VerReservaPoli = () => {
  const [reservasPoli, setReservasPoli] = useState([]);
  // const [horarios, setHorarios] = useState([]);
  // const [polideportivos, setPolideportivos] = useState([]);
  // const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);
  // const [currentDate, setCurrentDate] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState((new Date()).toISOString().split('T')[0]);
  // const [llegoReserva, setLlegoReserva] = useState({});
  const handleDateChange = (event) => {
    setSelectedDate(event.target.value);
  };

  // const isReservaDelDiaActual = (fecha) => {
  //   const reservaDate = new Date(fecha);
  //   const currentDateString = currentDate.toISOString().split('T')[0];
  //   return reservaDate.toISOString().split('T')[0] === currentDateString;
  // };

  // const filteredReservas = reservasPoli.filter(reservaPoli => {
  //   const reservaDate = new Date(reservaPoli.fecha);
  //   const selectedDateObject = new Date(selectedDate);
  //   return reservaDate.toISOString().split('T')[0] === selectedDateObject.toISOString().split('T')[0];
  // });

  // const handleLlegoChange = (id) => {
  //   setLlegoReserva((prevLlegoReserva) => ({
  //     ...prevLlegoReserva,
  //     [id]: !prevLlegoReserva[id],
  //   }));
  // };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const reservasResponse = await fetch('http://127.0.0.1:8000/adminapp/api/reservapolideportivos/');
        const reservasPoliData = await reservasResponse.json();
        setReservasPoli(reservasPoliData);

        // const horariosResponse = await fetch('http://127.0.0.1:8000/adminapp/api/horarios/');
        // const horariosData = await horariosResponse.json();
        // setHorarios(horariosData);

        // const polideportivosResponse = await fetch('http://127.0.0.1:8000/adminapp/api/polideportivos/');
        // const polideportivosData = await polideportivosResponse.json();
        // setPolideportivos(polideportivosData);

        // const usuariosResponse = await fetch('http://127.0.0.1:8000/adminapp/api/usuarios/');
        // const usuariosData = await usuariosResponse.json();
        // setUsuarios(usuariosData);

        setLoading(false);
      } catch (error) {
        console.error('Error fetching reservations:', error);
      }
    };

    fetchData();
  }, []);

  // const isReservaPasada = (fecha) => {
  //   const reservaDate = new Date(fecha);
  //   return reservaDate < currentDate;
  // };


  if (loading) {
    return <p>Cargando datos...</p>;
  }

  return (
    <div>
      <header className="bg-dark text-white">
        <div className="container py-2">
          <div className="d-flex flex-wrap align-items-center justify-content-center">
            <a href="/" className="d-flex align-items-center text-white text-decoration-none">
              <img src="/logo.png" alt="TECSITE Logo" width="120" height="120" className="logo" />
            </a>
          </div>
        </div>
      </header>

      <div className="container mt-4">
        <h2 className="mb-4">Reservas de Polideportivos</h2>

        <div className="mb-3">
          <label htmlFor="dateFilter" className="form-label">Filtrar por fecha:</label>
          <input
            type="date"
            id="dateFilter"
            className="form-control"
            value={selectedDate}
            onChange={handleDateChange}
          />
        </div>

        <table className="table table-striped table-bordered">
          <thead className="thead-dark">
            <tr>
              <th scope="col">Fecha de reserva</th>
              <th scope="col">Hora Inicio</th>
              <th scope="col">Hora Fin</th>
              <th scope="col">Nombre del polideportivo</th>
              <th scope="col">Cod. Estudiante</th>
            </tr>
          </thead>
          <tbody>
            {
              reservasPoli.map((reservaPoli) => {

                return (
                  <tr key={reservaPoli.id}>
                    <td>{reservaPoli.fecha}</td>
                    <td>{reservaPoli.Horario_inicio}</td>
                    <td>{reservaPoli.Horario_fin}</td>
                    <td>{reservaPoli.laboratorio.nombre}</td>
                    <td>{reservaPoli.usuario.codigo}</td>
                  </tr>
                )
              })
            }
          </tbody>
        </table>
        <div className="button-group">
          <a href="/" className="btn btn-lg btn-primary mt-3">Regresar</a>
        </div>
      </div>
    </div>
  );
};

export default VerReservaPoli;
