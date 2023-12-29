<?php

function LeerXML()
{
    $archivo = 'asesores.xml';
    $xml = simplexml_load_file($archivo);
    return $xml->asesor;
}
function EscribirXML()
{
    $archivo = 'asesores.xml';
    $datos = '
    <asesores>
    <asesor>
      <id>1</id>
      <password>password1</password>
      <ultimo_acceso>2023-07-29 12:34:56</ultimo_acceso>
      <operacion>consulta</operacion>
      <tiempo_conexion>120</tiempo_conexion>
    </asesor>
    <asesor>
    <id>2</id>
    <password>clave2</password>
    <ultimo_acceso>2023-07-29 10:15:30</ultimo_acceso>
    <operacion>eliminación</operacion>
    <tiempo_conexion>60</tiempo_conexion>
  </asesor>
  <asesor>
    <id>3</id>
    <password>password3</password>
    <ultimo_acceso>2023-07-29 14:20:45</ultimo_acceso>
    <operacion>actualización</operacion>
    <tiempo_conexion>180</tiempo_conexion>
  </asesor>
  <asesor>
    <id>4</id>
    <password>secret4</password>
    <ultimo_acceso>2023-07-29 16:40:22</ultimo_acceso>
    <operacion>inclusión</operacion>
    <tiempo_conexion>240</tiempo_conexion>
  </asesor>
  <asesor>
    <id>5</id>
    <password>confidential5</password>
    <ultimo_acceso>2023-07-29 08:55:12</ultimo_acceso>
    <operacion>consulta</operacion>
    <tiempo_conexion>90</tiempo_conexion>
  </asesor>
  </asesores>';

    file_put_contents($archivo, $datos);
    echo "Datos de asesores jurídicos escritos correctamente";
}

function CerrarXML()
{
    $archivo = 'asesores.xml';
    if (file_exists($archivo)) {
        if (unlink($archivo)) {
            echo "El archivo se cerro correctamente";
        } else {
            echo "Hubo un error al cerrar el archivo";
        }
    } else {
        echo "El archivo no existe";
    }
}





$variable = $_POST['opcion'];

switch ($variable) {
    case 'abrir':
        $asesores = LeerXML();
        echo '<h2>Asesores registrados</h2>';
        echo '<ul>';
        foreach ($asesores as $asesor) {
            echo '<li>ID: ' . $asesor->id . ', Contraseña: ' . $asesor->password . ', Ultima conexion: ' . $asesor->ultimo_acceso . ', Operacion: ' . $asesor->operacion . ', Tiempo de Conexion: ' . $asesor->tiempo_conexion . ' minutos</li>';
        }
        echo ' </ul>';
        break;
    case 'leer':
        $asesores = LeerXML();
        echo '<h2>Asesores registrados</h2>';
        echo '<ul>';
        foreach ($asesores as $asesor) {
            echo '<li>ID: ' . $asesor->id . ', Contraseña: ' . $asesor->password . ', Ultima conexion: ' . $asesor->ultimo_acceso . ', Operacion: ' . $asesor->operacion . ', Tiempo de Conexion: ' . $asesor->tiempo_conexion . ' minutos</li>';
        }
        echo ' </ul>';
        break;
    case 'escribir':
        EscribirXML();
        break;
    case 'cerrar':
        CerrarXML();
        break;
    default:
        echo "Opción no valida";
        break;
}
