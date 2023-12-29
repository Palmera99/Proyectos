<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
</head>

<body>
    <h1>Formulario de ingreso de notas</h1>
    <form action="respuesta.php" method="post">
        <label for="Nombre">Nombre: </label>
        <input type="text" name="Nombre" id="Nombre" required />
        <br />
        <label for="calif1">Calificacion 1: </label>
        <input type="text" name="calif1" id="calif1" required />
        <br />

        <label for="calif2">Calificacion 2: </label>
        <input type="text" name="calif2" id="calif2" required />
        <br />
        <label for="calif3">Calificacion 3: </label>
        <input type="text" name="calif3" id="calif3" required />
        <br />
        <label for="calif4">Calificacion 4: </label>
        <input type="text" name="calif4" id="calif4" required />
        <br />
        <label for="calif5">Calificacion 5: </label>
        <input type="text" name="calif5" id="calif5" required />
        <br />
        <input type="submit" value="Enviar" />
    </form>
</body>

</html>
<?php

$nombre = $_POST['Nombre'];

$calif1 = $_POST['calif1'];
$calif2 = $_POST['calif2'];
$calif3 = $_POST['calif3'];
$calif4 = $_POST['calif4'];
$calif5 = $_POST['calif5'];

$total = $calif1 + $calif2 + $calif3 + $calif4 + $calif5;
$total /= 5;
if ($total >= 9) {
    echo "El estudiante " . "<strong>" . $nombre . "<strong/>" . " tiene una calificacion final de " . $total . " y esta aprobado";
} else {
    echo "El estudiante " . $nombre . " tiene una calificacion final de " . $total . " y esta reprobado";
}
