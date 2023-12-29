<?php

class Curso
{
    private $codigo;
    private $nombre;
    private $duracion;
    private $fechainicio;
    private $fechafin;
    //Getters & Setters
    function setCodigo($codigo)
    {
        $this->codigo = $codigo;
    }
    function setNombre($nombre)
    {
        $this->nombre = $nombre;
    }
    function setDuracion($duracion)
    {
        $this->duracion = $duracion;
    }
    function setFechaInicio($fechainicio)
    {
        $this->fechainicio = $fechainicio;
    }
    function setFechaFin($fechafin)
    {
        $this->fechafin = $fechafin;
    }

    function getCodigo()
    {
        return $this->codigo;
    }
    function getNombre()
    {
        return $this->nombre;
    }
    function getDuracion()
    {
        return $this->duracion;
    }
    function getFechaInicio()
    {
        return $this->fechainicio;
    }
    function getFechaFin()
    {
        return $this->fechafin;
    }
}

$curso1 = new Curso();
$curso1->setCodigo($_POST['cod']);
$curso1->setNombre($_POST['nombre']);
$curso1->setDuracion($_POST['duracion']);
$curso1->setFechaInicio($_POST['fechainicio']);
$curso1->setFechaFin($_POST['fechafin']);

echo '<table>';
echo '<tr><td>Código del curso</td><td>' . $curso1->getCodigo() . '</td></tr>';
echo '<tr><td>Nombre del curso</td><td>' . $curso1->getNombre() . '</td></tr>';
echo '<tr><td>Duración del curso</td><td>' . $curso1->getDuracion() . ' Horas</td></tr>';
echo '<tr><td>Fecha de inicio del curso</td><td>' . $curso1->getFechaInicio() . '</td></tr>';
echo '<tr><td>Fecha de término del curso</td><td>' . $curso1->getFechaFin() . '</td></tr>';
echo '</table>';
