<?php


class Conexion
{
    public static function conexionDB()
    {
        $server = "localhost";
        $user = "root";
        $pass = "lollol";
        $db = "primera";
        try {
            $conexion = new PDO("mysql:host=$server;dbname=$db", $user, $pass);
            echo "conexion correcta";
        } catch (PDOException $error) {
            echo ("no se conecto" . $error);
        }
        return $conexion;
    }
}
