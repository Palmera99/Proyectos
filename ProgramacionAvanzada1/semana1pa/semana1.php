<?php

class Vehiculos{
    public function __construct(    
    public $marca,
    public $modelo,
    public $anio,
    public $numpuertas,
    public $rutpropietario)
    {
      
    }
}

$v1 = new Vehiculos(
    "suzuki",
    'baleno',
    2001,
    5,
    20049728-7
);

$v2 = new Vehiculos(
    "morris garage",
    "mg3",
    2017,
    5,
    16713373-8
);

var_dump($v1);
echo "<br>";
var_dump($v2);