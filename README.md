"Clinica_PC" 
Aplicacion que Simula una clinica de computadoras
Pasos para el uso de la clinica:
1. Clonar el repositorio
2. Crear un entorno virtual (python -m venv nombre_entorno)
3. Instalar las dependencias(pip install -r requirements.txt)
4. Configurar el archivo .env debe ser creado por el usuario este archivo usara estos datos

Estructura del env para la conexion a base de datos
MI_ENGINE='django.db.backends.postgresql'  (Motor de base de datos)
MI_NAME= "db_clinica_pc"   (Nombre de la base de datos)
MI_USER= "postgres"   (Usuario de la base de datos)
MI_PASSWORD="12345678"   (Contraseña de la base de datos)
MI_HOST="localhost"   (Host de la base de datos)
MI_PORT="5432"   (Puerto de la base de datos)

5. Hacer las migraciones para que funcione la base de datos (python manage.py migrate)
6. Iniciar el servidor (python manage.py runserver)
El servidor se iniciara en http://127.0.0.1:8000/

Logica de uso:
1. Iniciar sesion con el usuario inacap y la contraseña clinica2025
2. Recepcion aqui se ingresaran los nuevos equipos a la clinica y revisar los equipos que ya estan ingresados
3. Diagnostico aqui se podra hacer el diagnostico del equipo y revisar equipos que ya han sido diagnosticados
4. Entrega aqui se podra revisar los equipos de la clinica y confirmar su estado tambien se podran realizar entregas y confirmar los comprobantes de las entregas

API Rest 
La aplicacion cuenta con una API Rest que permite hacer operaciones CRUD con los equipos de la clinica con Postman las apis estan en los siguientes enlances:
http://127.0.0.1:8000/recepcion/api/listado/
estructura del listado
    {
        "id": 4,
        "cliente": "SuperCliente",
        "equipo": "SuperEquipo",
        "problema": "Existe"
    },

http://127.0.0.1:8000/recepcion/api/agregar/ (estructura del agregar)
{
    "cliente": "SuperCliente",
    "equipo": "SuperEquipo",
    "problema": "Existe"
}

http://127.0.0.1:8000/recepcion/api/actualizar/<int:pk>/ (pk debe dar la id del objeto que se vaya a actualizar por ejemplo 4)
{
    "cliente": "SuperCliente",
    "equipo": "SuperEquipo",
    "problema": "Existe"
}

http://127.0.0.1:8000/recepcion/api/eliminar/<int:pk>/ (pk debe dar la id del objeto que se vaya a eliminar) no requiere estructura solo el id)


