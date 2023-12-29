<?php

abstract class Vehiculo2
{
    protected $modelo;
    protected $anio;

    public function __construct($modelo, $anio)
    {
        $this->modelo = $modelo;
        $this->anio = $anio;
    }

    abstract public function imprimirmodelo();
    abstract public function imprimiranio();
}

class Auto extends Vehiculo2
{
    public function imprimirmodelo()
    {
        echo "Modelo: " . $this->modelo . "<br>";
    }
    public function imprimiranio()
    {
        echo "año: " . $this->anio . "<br>";
    }
}
echo "<h1>";
$Auto1 = new Auto("Baleno", 2001);
$Auto1->imprimirmodelo();
$Auto1->imprimiranio();
echo "</h1>";
?>

<?php

interface MensajeInterface
{
    public function ImprimirMensaje1();
    public function ImprimirMensaje2();
}

class MiClase implements MensajeInterface
{
    public function ImprimirMensaje1()
    {
        echo "Primer Mensaje <br>";
    }
    public function ImprimirMensaje2()
    {
        echo "Segundo Mensaje <br>";
    }
}
echo "<h1>";
$miclase = new MiClase();
$miclase->ImprimirMensaje1();
$miclase->ImprimirMensaje2();
echo "</h1>";
?>

<?php

$vehiculo = new class
{
    private $nombreauto = "Suzuki";

    public function getnombre()
    {
        return $this->nombreauto;
    }
};
echo "<h1>";
echo $vehiculo->getnombre();
echo "</h1>";

?>
