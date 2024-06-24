import React, { useEffect, useState } from 'react';

const VerReservaLab = () => {
  const [reservasLab, setReservasLab] = useState([]);
  // const [horarios, setHorarios] = useState([]);
  // const [laboratorios, setLaboratorios] = useState([]);
  // const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);
  // const [currentDate, setCurrentDate] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState((new Date()).toISOString().split('T')[0]);
  // const [llegoReservaLocal, setLlegoReservaLocal] = useState({});
  const handleDateChange = (event) => {
    setSelectedDate(event.target.value);
  };

  // const isReservaDelDiaActual = (fecha) => {
  //   const reservaDate = new Date(fecha);
  //   const currentDateString = currentDate.toISOString().split('T')[0];
  //   return reservaDate.toISOString().split('T')[0] === currentDateString;
  // };

  // const filteredReservas = reservasLab.filter((reservaLab) => {
  //   const reservaDate = new Date(reservaLab.fecha);
  //   const selectedDateObject = new Date(selectedDate);
  //   return (
  //     reservaDate.toISOString().split('T')[0] === selectedDateObject.toISOString().split('T')[0]
  //   );
  // });

  // const handleLlegoChange = (id) => {
  //   setLlegoReservaLocal((prevLlegoReservaLocal) => ({
  //     ...prevLlegoReservaLocal,
  //     [id]: !prevLlegoReservaLocal[id],
  //   }));
  // };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const reservasResponse = await fetch('http://127.0.0.1:8000/adminapp/api/reservalaboratorios/');
        const reservasLabData = await reservasResponse.json();
        setReservasLab(reservasLabData);

        // const horariosResponse = await fetch('http://127.0.0.1:8000/adminapp/api/horarios/');
        // const horariosData = await horariosResponse.json();
        // setHorarios(horariosData);

        // const laboratoriosResponse = await fetch('http://127.0.0.1:8000/adminapp/api/laboratorios/');
        // const laboratoriosData = await laboratoriosResponse.json();
        // setLaboratorios(laboratoriosData);

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
        <h2 className="mb-4">Reservas de Laboratorios</h2>

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
              <th scope="col">Nombre del laboratorio</th>
              <th scope="col">Cod. Estudiante</th>
            </tr>
          </thead>
          <tbody>
            {
              reservasLab.map((reserva) => {

                return (
                  <tr key={reserva.id}>
                    <td>{reserva.fecha}</td>
                    <td>{reserva.Horario_inicio}</td>
                    <td>{reserva.Horario_fin}</td>
                    <td>{reserva.laboratorio.nombre}</td>
                    <td>{reserva.usuario.codigo}</td>
                    {/* <td>{reserva.usuario.codigo}</td> */}
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

export default VerReservaLab;
