
<?php
session_start();

// Configuración inicial
$cartName = "mi_carrito";
$totalPrice = 0;
$products = [
    ["id" => 1, "name" => "Producto 1", "description" => "Libro 1", "price" => 10990],
    ["id" => 2, "name" => "Producto 2", "description" => "Libro 2", "price" => 19990],
    ["id" => 3, "name" => "Producto 3", "description" => "Libro 3", "price" => 5990],
    ["id" => 4, "name" => "Producto 4", "description" => "Libro 4", "price" => 5990],
    ["id" => 5, "name" => "Producto 5", "description" => "Libro 5", "price" => 5990]
];

// Agregar producto al carrito
if (isset($_POST['product_id'])) {
    $productId = $_POST['product_id'];

    if (isset($_SESSION[$cartName][$productId])) {
        $_SESSION[$cartName][$productId]['quantity']++;
    } else {
        $_SESSION[$cartName][$productId] = [
            'quantity' => 1,
            'price' => $products[$productId - 1]['price']
        ];
    }
}

// Mostrar lista de productos
echo "<h1>Productos</h1>";
echo "<table>";
echo "<tr><th>Nombre</th><th>Descripción</th><th>Precio</th><th></th></tr>";
foreach ($products as $product) {
    echo "<tr>";
    echo "<td>" . $product['name'] . "</td>";
    echo "<td>" . $product['description'] . "</td>";
    echo "<td>$" . $product['price'] . "</td>";
    echo "<td><form action='index.php' method='post'>
            <input type='hidden' name='product_id' value='" . $product['id'] . "'/>
            <input type='submit' value='Agregar al carrito'/>
        </form></td>";
    echo "</tr>";
}
echo "</table>";

// Mostrar carrito
echo "<h1>Carrito de compras</h1>";
echo "<table>";
echo "<tr><th>Nombre</th><th>Cantidad</th><th>Precio Unitario</th><th>Subtotal</th><th></th></tr>";
foreach ($_SESSION[$cartName] as $productId => $item) {
    $product = $products[$productId - 1];
    $subtotal = $item['quantity'] * $product['price'];

    echo "<tr>";
    echo "<td>" . $product['name'] . "</td>";
    echo "<td>" . $item['quantity'] . "</td>";
    echo "<td>$" . $product['price'] . "</td>";
    echo "<td>$" . $subtotal . "</td>";
    echo "<td><a href='remove.php?product_id=" . $product['id'] . "'>Eliminar</a></td>";
    echo "</tr>";
    $totalPrice += $subtotal;
}
echo "<tr><td colspan='3'>Precio Total:</td><td>$" . $totalPrice . "</td></tr>";
echo "</table>";
?>
