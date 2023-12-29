<?php
require 'vendor/autoload.php';

// Función para leer los datos de los asesores desde el archivo XML
function leerAsesores()
{
  $archivo = 'asesores.xml';
  $xml = simplexml_load_file($archivo);
  return $xml->asesor;
}

// Función para formatear los datos de los asesores en una tabla HTML
function generarTablaAsesores($asesores)
{
  $table = '<table border="1">';
  $table .= '<tr><th>ID</th><th>Contraseña</th><th>Último Acceso</th><th>Operación</th><th>Tiempo de Conexión</th></tr>';

  foreach ($asesores as $asesor) {
    $table .= '<tr>';
    $table .= '<td>' . $asesor->id . '</td>';
    $table .= '<td>' . $asesor->password . '</td>';
    $table .= '<td>' . $asesor->ultimo_acceso . '</td>';
    $table .= '<td>' . $asesor->operacion . '</td>';
    $table .= '<td>' . $asesor->tiempo_conexion . '</td>';
    $table .= '</tr>';
  }

  $table .= '</table>';

  return $table;
}

// Obtener los datos de los asesores desde el archivo XML
$asesores = leerAsesores();

// Generar el contenido del informe PDF con la tabla de asesores
$data = '
<h1>Informe de Asesores Jurídicos</h1>
<p>En este informe se detallan los asesores registrados y sus actividades.</p>
' . generarTablaAsesores($asesores) . '
';
$pdf = new Spipu\Html2Pdf\Html2Pdf();
$pdf->writeHTML($data);
$pdf->output('informe.pdf');
