<?php
session_start();

if (isset($_GET['product_id'])) {
    $productId = $_GET['product_id'];

    if (isset($_SESSION['mi_carrito'][$productId])) {
        unset($_SESSION['mi_carrito'][$productId]);
    }
}

header("Location: index.php");
exit;
