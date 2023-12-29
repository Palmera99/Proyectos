<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="tarea1.php" method="post">
        <table>
            <tr>
                <td><label for="nombre">Nombre:</label></td>
                <td><input type="text" name="nombre" id="nombre"></td>
            </tr>
            <tr>
                <td><label for="apellido">Apellido</label></td>
                <td><input type="text" name="apellido" id="apellido"></td>
            </tr>
            <tr>
                <td><label for="rut">Rut</label></td>
                <td><input type="text" name="rut" id="rut"></td>
            </tr>
        </table>
        <input type="submit" value="enviar">
    </form>

    <?php
    session_start();
    if (isset($_POST["nombre"]) && isset($_POST["apellido"]) && isset($_POST["rut"])) {
        $nombre = $_POST["nombre"];
        $apellido = $_POST["apellido"];
        $rut = $_POST["rut"];

        $_SESSION["nombre"] = $nombre;
        $_SESSION["apellido"] = $apellido;
        $_SESSION["rut"] = $rut;

        echo $_SESSION["nombre"] . "<br>";
        echo $_SESSION["apellido"] . "<br>";
        echo $_SESSION["rut"] . "<br>";
    }

    ?>
</body>

</html>