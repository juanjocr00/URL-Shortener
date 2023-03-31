
# Prueba Técnica Sunwise

## Acortador de URLs con Django
Este proyecto es una Rest API hecha con Django en Python que permite a los usuarios acortar URLs largas y acceder a ellas de manera más fácil y rápida. Además, cuenta con un sistema de autenticación para los usuarios y ofrece la posibilidad de crear URLs públicas o privadas.

### Funciones
#### Acortar URL
El usuario puede ingresar una o varias URLs largas y el programa les devuelve una URL acortada. La URL acortada también se puede personalizar para hacerla más fácil de recordar.

#### Redirección a la página
Los usuarios pueden ser redirigidos a la página original a través de la URL acortada. Además, se lleva un registro del número de veces que se ha visitado la página de redirección de la URL acortada.

#### Inicio de Sesión, Salida de Sesión y Registro de Usuario
El programa cuenta con un sistema de autenticación de usuarios para proteger las URLs privadas. Los usuarios pueden iniciar sesión, cerrar sesión y registrarse para acceder a esta funcionalidad.

#### Verificación de URLs
El programa verifica si las URLs ingresadas por los usuarios son válidas.

#### Parámetros en el modelo
El modelo de la base de datos incluye los siguientes parámetros: URL original, URL acortada, número de veces visitada la página de redirección de la URL acortada, usuario que solicitó el acortamiento de la URL y si la URL acortada es pública o privada.

#### Ingresar manualmente las URLS
Cuenta con una área de texto para introducir de forma manual una o más URLs separadas por una separación de lineas para luego generar URLs acortadas.

#### Subida de archivos .txt
El usuario puede subir un archivo .txt a la aplicación con varias URLs separadas por líneas. La aplicación leerá el archivo y acortará cada una de las URLs.

#### URLs públicas y privadas
Las URLs acortadas pueden ser públicas o privadas. Las URLs públicas son accesibles para cualquier usuario sin necesidad de iniciar sesión. Las URLs privadas sólo son accesibles para el usuario que solicitó el acortamiento de la URL y que ha iniciado sesión.

## Instalación y Deploy

Al descargar la carpeta del proyecto, se deberá hacer un entorno virtual dentro de la carpeta.

Abrir una terminal dentro de la carpeta del proyecto y correr:
```bash
  python -m venv my_env
```

Activar el entorno virtual
```bash
  .\my_env\Scripts\activate
```

Instalar los requerimientos del archivo requirements.txt
```bash
  python -m pip install -r requirements.txt
```
Iniciar el servidor
```bash
  python manage.py runserver
```
    

## Capturas de Pantalla
Home
![App Screenshot](https://i.imgur.com/N2XXN6v.png)
Log In
![App Screenshot](https://i.imgur.com/gqJ6zuo.png)
Input Manual de URLs
![App Screenshot](https://i.imgur.com/SnB0cQ6.png)
Subir archivo .txt
![App Screenshot](https://i.imgur.com/jRXJhcG.png)


## Instrucciones de la prueba

### Ejercicio 2
Descripción
La siguiente prueba consiste en construir los servicios web necesarios usando como referencia API REST FULL, los servicios web deben ser capaz de acortar URLS en general, usar Django (preferentemente).

#### Instrucciones
Utiliza Git para Documentar tus avances.

Al finalizar este ejercicio proporciona la url del repositorio público, este debe contener un archivo README que explique exactamente los pasos necesarios para construir y ejecutar el proyecto.

Proporciona la documentación de los servicios web, puedes usar Postman o swagger.

#### Generalidades

Las url’s podrán ser de 2 tipos públicas y privadas, las url’s privadas solo podran ser accedidas si existe un token de usuario.
Guardar el # de vistas de la url y el usuario que accedio (en caso de tener un usuario autenticado.
Debo poder editar y eliminar únicamente la url.
Registro de usuario simple con correo y contraseña.
El usuario registrado deberá poder iniciar sesión.
Tareas

Crear un servicio web capaz de acortar url’s, por ejemplo, si se recibe la URL “https://facebook.com” se debería devolver “http://host/Ux26Yp”.
Crear un servicio web para que cuando alguien acceda a la URL “https://host/Ux26Yp”, el servidor redireccione a la URLcorrespondiente “https://facebook.com”.
Crear un servicio web capaz de recibir una lista de urls (incluir url privadas), esta deberá retornar la lista de url’s acortadas.
Crear un servicio que regrese una lista paginada de 20 registros de todas las URL’s, su versión corta, # de vistas, usuario que accedio (no importa si es pública o privada).
#### Extras (opcionales), pudes usar html, javascript, react, vue… cualquier otra.

Crear una interfaz web que permita a los usuarios enviar una url para acortarla.
Agregar a la interfaz una opción para enviar un archivo de texto lleno de URL’s, esto deberá ser enviado a la API masiva. Los resultados pueden presentarse directamente en la página y descargarse como un archivo de texto.
Registro y Login de usuarios.