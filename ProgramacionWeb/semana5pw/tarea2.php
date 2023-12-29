<?php

function contarimpares()
{
    $contador = 0;
    for ($i = 1; $i <= 50; $i++) {
        if ($i % 2 != 0) {
            $contador++;
        }
    }


    return $contador;
}

$impares = contarimpares();
echo "la cantidad de impares es: " . $impares;
