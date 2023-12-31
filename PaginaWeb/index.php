<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css">
    <title>Bengu.Art</title>
</head>

<body>
    <header>
        <!--Logo-->
        <a href="#" target="" rel="noopener noreferrer">
            <img src="Logo.jpg" alt="Logo" height="80px" width="95px" /></a>
        <!--Nombre-->
        <a href="#" target="" rel="noopener noreferrer">
            <h1>Bengu.Art</h1>
        </a>
    </header>
    <section class="contenido">
        <?php
    $directorio = 'Imagenes'; // Ruta de tu carpeta con las imágenes
    $archivos = scandir($directorio);

    foreach ($archivos as $archivo) {
      if ($archivo !== '.' && $archivo !== '..') {
        echo '<img src="' . $directorio . '/' . $archivo . '" alt="Descripción de la imagen" height="200px" width="200px">';
      }
    }
    ?>

    </section>
    <footer>
        <ul class="sci">
            <li><a href="#">
                    <ion-icon name="logo-facebook"></ion-icon>
                </a></li>
            <li><a href="#">
                    <ion-icon name="logo-instagram"></ion-icon>
                </a></li>
            <li><a href="#">
                    <ion-icon name="logo-whatsapp"></ion-icon>
                </a></li>
        </ul>
    </footer>
</body>
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>

</html>