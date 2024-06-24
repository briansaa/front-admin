from django.db import models


class Usuario(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    codigo = models.CharField(max_length=50, unique=True, db_column="t_code")
    email = models.EmailField(max_length=255, unique=True, db_column="t_email")
    contrasena = models.CharField(max_length=25, db_column="t_password")

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = "t_member"
        managed = False


class Polideportivo(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "t_polideportivo"
        managed = False


class TipoLaboratorio(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    nombre = models.CharField(max_length=255, db_column="t_name")
    descripcion = models.CharField(max_length=255, db_column="t_description")

    class Meta:
        db_table = "t_educational_and_recreational_facility_type"


class Pabellon(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    nombre = models.CharField(max_length=255, db_column="t_name")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "t_educational_and_recreational_pavilion"
        managed = False


class Laboratorio(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    nombre = models.CharField(max_length=255, db_column="t_description")
    tipo = models.ForeignKey(
        TipoLaboratorio,
        on_delete=models.CASCADE,
        db_column="t_educational_and_recreational_facilities_type_identifier",
    )
    pabellones = models.ManyToManyField(Pabellon, through="PabellonLaboratorio")

    class Meta:
        db_table = "t_educational_and_recreational_facility"
        managed = False


class PabellonLaboratorio(models.Model):
    pabellon = models.ForeignKey(
        Pabellon,
        on_delete=models.CASCADE,
        db_column="t_recreational_pavilion_identifier",
    )
    item = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        db_column="t_educational_facility_identifier",
    )

    class Meta:
        db_table = "t_edu_rec_fac_and_t_rec_pav"
        managed = False


class Horario(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    hora_inicio = models.TimeField(db_column="lt_start_time")
    hora_fin = models.TimeField(db_column="lt_end_time")

    def __str__(self):
        return (
            f"{self.hora_inicio.strftime('%H:%M')} a {self.hora_fin.strftime('%H:%M')}"
        )

    class Meta:
        db_table = "t_educational_and_recreational_facility_hour"
        managed = False


class ReservaLaboratorio(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, db_column="identifier", max_length=36
    )
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        default=0,
        db_column="t_educational_and_recreational_facility_identifier",
    )
    fecha = models.DateTimeField(db_column="d_reservation")
    Horario_inicio = models.TimeField(db_column="lt_reservation_start_time")
    Horario_fin = models.TimeField(db_column="lt_reservation_end_time")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1, db_column="t_member_identifier")

    def __str__(self):
        return f"{self.laboratorio.nombre} - {self.Horario} - {self.Usuario.codigo}"

    class Meta:
        db_table = "t_reservation"
        managed = False


class ReservaPolideportivo(models.Model):
    polideportivo = models.ForeignKey(
        Polideportivo, on_delete=models.CASCADE, default=0
    )
    fecha = models.DateField()
    Horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.polideportivo.nombre} - {self.Horario} - {self.Usuario.codigo}"
