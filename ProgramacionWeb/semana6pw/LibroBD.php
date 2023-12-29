<?php
$titulo = $_POST['titulo'];
$autores = $_POST['autores'];
$editorial = $_POST['editorial'];
$anio = $_POST['anio'];
$genero = $_POST['genero'];
$isbn = $_POST['isbn'];
if (isset($_POST['ingresar'])) {
    $ingresar = $_POST['ingresar'];
} else {
    $ingresar = '';
}
if (isset($_POST['modificar'])) {
    $modificar = $_POST['modificar'];
} else {
    $modificar = '';
}
if (isset($_POST['consultar'])) {
    $consultar = $_POST['consultar'];
} else {

    $consultar = '';
}
if ($titulo != '' && $autores != '' && $editorial != '' && $anio != '' && $genero != '' && $isbn != '') {
    $user = "root";
    $password = 'lollol';
    $bd = "iacc";
    $host = "localhost";
    $result = NULL;
    $exito = 0;
    $mysqli = new mysqli($host, $user, $password, $bd);
    if ($mysqli != NULL) {
        if ($ingresar == 'Ingresar') {
            $query = "insert into libros values('" . $titulo . "', '" . $autores . "', '" . $editorial . "', " . $anio . ", '" .
                $genero . "', '" . $isbn . "')";
            $result = $mysqli->query($query);
            if ($result === TRUE) {
                echo "<br/><center><a href='./registroLibros.html'>Registro exitoso, haga clic aqui para
regresar<a></center>";
            }
        }
        if ($modificar == 'Modificar') {
            $query = "update libros set titulo='" . $titulo . "', autores='" . $autores . "', editorial='" . $editorial . "',
anio=" . $anio . ", genero='" . $genero . "', isbn='" . $isbn . "'" . " where isbn='" . $isbn . "'";
            $result = $mysqli->query($query);
            if ($result == TRUE) {
                echo "<br/><center><a href='./registroLibros.html'>Modificación exitosa, haga clic aqui para
regresar<a></center>";
            }
        }
        $mysqli->close();
    }
} else if ($isbn != '') {
    $user = "root";
    $password = 'lollol';
    $bd = "iacc";
    $host = "localhost";
    $result = NULL;
    $exito = 0;
    $mysqli = new mysqli($host, $user, $password, $bd);
    if ($mysqli != NULL) {
        if ($consultar == 'Consultar') {
            $query = "select * from libros where isbn='" . $isbn . "'";

            $result = $mysqli->query($query);
            echo "<table border='2' align='center'>";
            echo "<caption>Libro Consultado</caption>";
            while ($row = $result->fetch_assoc()) {
                echo "<tr bgcolor='cyan'><td>Título</td><td>Autores</td><td>Editorial</td><td>Año</td><td>Genero</td><td>ISBN</td></tr>";
                printf("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>", $row['titulo'], $row['autores'], $row['editorial'], $row['anio'], $row['genero'], $row['isbn']);
                $exito = 1;
            }
            echo "</table>";
            if ($exito == 0) {
                echo "<br/><center><a href='./registroLibros.html'>Libro NO registrado, haga clic aqui para
regresar<a></center>";
            } else {
                echo "<br/><center><a href='./registroLibros.html'>Consulta exitosa, haga clic aqui para
regresar<a></center>";
            }
        }
    }
    $mysqli->close();
} else {
    echo "Debe ingresar todos los datos para ingresar o modificar algún libro.<br/>";
    echo "Para consultar
sólo debe ingresar el ISBN.<br/>";
    echo "<br/><a href='./registroLibros.html'>Haga clic aqui para regresar<a>";
}
