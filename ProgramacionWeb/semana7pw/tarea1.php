<?php

#creamos una clase pantilla para reutilizar codigo y formar herencia
abstract class plantilla
{
    protected $nombre;

    public function __construct($nombre)
    {
        $this->nombre = $nombre;
    }
    public function getnombre()
    {
        return $this->nombre;
    }

    abstract public function MostrarInformacion();
}

class docente extends plantilla
{
    private $especialidad;

    public function __construct($nombre, $especialidad)
    {
        parent::__construct($nombre);
        $this->especialidad = $especialidad;
    }

    public function getespecialidad()
    {
        $this->especialidad;
    }
    public function MostrarInformacion()
    {
        echo "Nombre docente {$this->getnombre()}, con la especialidad en {$this->especialidad} </br>";
    }
}

class carrera extends plantilla
{

    private $duracion;

    public function __construct($nombre, $duracion)
    {
        parent::__construct($nombre);
        $this->duracion = $duracion;
    }

    public function getduracion()
    {
        return $this->duracion;
    }

    public function MostrarInformacion()
    {
        echo "Nombre carrera: {$this->getnombre()}, con la duracion de {$this->duracion} años </br>";
    }
}

class materias extends plantilla
{

    private $vecessemana;
    private  $docente;

    public function __construct($nombre, $vecessemana, $docente)
    {
        parent::__construct($nombre);
        $this->vecessemana = $vecessemana;
        $this->docente = $docente;
    }

    public function getvecessemana()
    {
        return $this->vecessemana;
    }
    public function getdocente()
    {
        return $this->docente;
    }

    public function MostrarInformacion()
    {
        echo "Nombre materia: {$this->getnombre()} con {$this->vecessemana} veces en la semana. Docente a cargo: {$this->docente->getnombre()} </br>";
    }
}
$primero = new docente("Francisco", "Programacion Web");
$segundo = new carrera("programacion", 4);
$tercero = new materias("programacion orientada a objetos", 3, $primero)

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $primero->MostrarInformacion();
    $segundo->MostrarInformacion();
    $tercero->MostrarInformacion();
    ?>
</body>

</html>