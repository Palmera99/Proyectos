//// See https://aka.ms/new-console-template for more information
//using System.Diagnostics.Tracing;

//Console.WriteLine("Hello, World!");


//var array = new int[] {1,2,3,4,5,6,7,8,9,10 };



//for (int i = 9; i >= 0; i--)
//{
//    Console.WriteLine(array[i]);
//}
//int value;

//value = 5;

//bool condicion = true;

//if (value > 0)
//{
//    int value2 = 6;


//}

//Console.WriteLine(value);

//if (condicion)
//    Console.WriteLine(condicion);
//int v = 5;

//switch (value)
//{
//    case 5:
//        Console.WriteLine("EL numero es 5");
//        break;
//    case 11:
//        Console.WriteLine("el numero es 11");
//        break;
//    default:
//        Console.WriteLine("El numero no es 5 ni 11");
//        break;
//}

//int[] numbers = { 4, 8, 15, 16, 23, 42 };

//foreach (int number in numbers)
//{
//    int total;

//    total =+ number;

//    if (number == 42)
//    {
//       bool found = true;
//    }

//}

using System.Reflection.PortableExecutable;

var idMascota = new List<string>();
var especieMascota = new List<string>();
var edadMascota = new List<string>();
var aparienciaMascota = new List<string>();
var personalidadMascota = new List<string>();
var nombreMascota = new List<string>();

var menu = true;

while (menu)
{
    Console.WriteLine("----Menu Principal----");
    Console.WriteLine("1. Mostrar Informacion de las mascotas");
    Console.WriteLine("2. Agregar una mascota");
    Console.WriteLine("3. Editar edad de mascota");
    Console.WriteLine("4. Edite personalidad de la mascota");
    Console.WriteLine("5. mostrar solo los perros");
    Console.WriteLine("6. Mostrar solo los gatos");
    Console.WriteLine("7. Salir");
    var respesta = Console.ReadLine();

    switch (respesta)
    {
        case "1":
            Console.WriteLine("----Lista de Mascotas----");
            for (int i = 0; i < idMascota.Count; i++)
            {
                Console.WriteLine($"ID: {idMascota[i]}, Nombre: {nombreMascota[i]}, Especie: {especieMascota[i]}, Edad: {edadMascota[i]}, Apariencia: {aparienciaMascota[i]}, Personalidad: {personalidadMascota[i]}");
            }
            break;
        case "2":
            Console.WriteLine("----Creacion de Mascotas----");
            Console.WriteLine("Ingrese ID");
            var id = Console.ReadLine();
            Console.WriteLine("Ingrese especie");
            var especie = Console.ReadLine();
            Console.WriteLine("Ingrese edad");
            var edad = Console.ReadLine();
            Console.WriteLine("Ingrese apariencia");
            var apariencia = Console.ReadLine();
            Console.WriteLine("Ingrese personalidad");
            var personalidad = Console.ReadLine();
            Console.WriteLine("Ingrese nombre");
            var nombre = Console.ReadLine();
            idMascota.Add(id.ToUpper());
            especieMascota.Add(especie.ToUpper());
            edadMascota.Add(edad.ToUpper());
            aparienciaMascota.Add(apariencia.ToUpper());
            personalidadMascota.Add(personalidad.ToUpper());
            nombreMascota.Add(nombre.ToUpper());
            break;
        case "3":
            Console.WriteLine("----Editar edad----");
            Console.WriteLine("Ingrese el ID de la mascota a editar");
            var idEditar = Console.ReadLine();
            for (int i = 0; i < idMascota.Count(); i++)
            {
                if (idMascota[i] == idEditar)
                {
                    Console.WriteLine($"El nombre de la mascota es: {nombreMascota[i]}");
                    Console.WriteLine("Ingrese la nueva edad");
                    var edadeditar = Console.ReadLine();
                    edadMascota[i] = edadeditar;
                    Console.WriteLine("Edad actualizada");
                }
                else
                {
                    Console.WriteLine("No se encontro la mascota");
                }
            }
            break;
        case "4":
            Console.WriteLine("----Editar Personalidad----");
            Console.WriteLine("Ingrese Id de la mascota");
            var ideditar = Console.ReadLine();
            for (int i = 0; i < idMascota.Count(); i++)
            {
                if (idMascota[i] == ideditar)
                {
                    Console.WriteLine($"El nombre de la mascota es: {nombreMascota[i]}");
                    Console.WriteLine("Ingrese la nueva personalidad");
                    var personalidadeditar = Console.ReadLine();
                    personalidadMascota[i] = personalidadeditar;
                    Console.WriteLine("Personalidad actualizada");
                }
                else
                {
                    Console.WriteLine("No se encontro la mascota");
                }
            }
            break;
        case "7":
            menu = false;
            break;
        default:
            Console.WriteLine("Alerta!! Debe de agregar un caracter sugerido");
            break;
    }

        



    
}
