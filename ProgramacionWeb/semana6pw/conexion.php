<?php
function conexion()
{
    $host = "localhost";
    $user = "root";
    $pass = "lollol";
    $db  = "academia";

    try {
        $conexion = mysqli_connect($host, $user, $pass, $db);
    } catch (\Throwable $th) {
        die("no se pudo conectar" . mysqli_error($conexion));
    }

    return $conexion;
}

$codigo = $_POST['cod'];
$nombre = $_POST['nombre'];
$duracion = $_POST['duracion'];
$fechainicio = $_POST['fechainicio'];
$fechafin = $_POST['fechafin'];

if (isset($_POST['enviar'])) {
    $enviar = $_POST['enviar'];
} else {
    $enviar = '';
}
if (isset($_POST['consultar'])) {
    $consultar = $_POST['consultar'];
} else {
    $consultar = '';
}
if (isset($_POST['modificar'])) {
    $modificar = $_POST['modificar'];
} else {
    $modificar = '';
}
if ($codigo != '' && $nombre != '' && $duracion != '' && $fechainicio != '' && $fechafin != '') {
    $conectar = conexion();
    $resultado = null;
    $exito = 0;
    if ($enviar == 'Enviar') {
        $query = "insert into cursos values(" . $codigo . ",'" . $nombre . "', " . $duracion . ", '" . $fechainicio . "', '" . $fechafin . "')";
        $resultado = $conectar->query($query);
        if ($resultado === true) {
            echo "<br/><center><a href='./formulario1.html'>Registro exitoso, haga clic aqui para
        regresar<a></center>";
        }
    }
    if ($modificar == 'Modificar') {
        $query = "update cursos set codigo = " . $codigo . ", nombre = '" . $nombre . "', " . $duracion . ", '" . $fechainicio . "', '" . $fechafin . "'" . "where codigo = " . $codigo . "";
        $resultado = $conectar->query($query);
        if ($resultado === true) {
            echo "<br/><center><a href='./formulario1.html'>Modificacion exitosa, haga clic aqui para
regresar<a></center>";
        }
    }
    $conectar->close();
} elseif ($codigo != '') {
    $conectar = conexion();
    $exito = 0;
    $resultado = null;
    if ($conectar != NULL) {
        if ($consultar == 'Consultar') {
            $query = "Select * from cursos where codigo = " . $codigo . "";
            $resultado = $conectar->query($query);
            echo "<table border='2' align='center'>";
            echo "<caption>Curso Consultado</caption>";

            while ($row = $resultado->fetch_assoc()) {
                echo "<tr bgcolor='cyan'><td>Codigo</td><td>Nombre</td><td>Duracion</td><td>Fecha Inicio</td><td>Fecha Fin</td></tr>";
                printf("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>", $row['codigo'], $row['nombre'], $row['duracion'], $row['fechainicio'], $row['fechafin'],);
                $exito = 1;
            }
            echo "</table>";
            if ($exito == 0) {
                echo "<br/><center><a href='./formulario1.html'>Curso NO registrado, haga clic aqui para
regresar<a></center>";
            } else {
                echo "<br/><center><a href='./formulario1.html'>Consulta exitosa, haga clic aqui para
regresar<a></center>";
            }
        }
    }
} else {
    echo "Debe ingresar todos los datos para ingresar o modificar algún Curso.<br/>";
    echo "Para consultarsólo debe ingresar el Codigo.<br/>";
    echo "<br/><a href='./formulario1.html'>Haga clic aqui para regresar<a>";
}
