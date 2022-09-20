# Niveles de usuario

## Usuario nivel 1 

Este usuario es el usuario con mayor poder, puede:

* Crear
* Actualizar
* Consultar
* Eliminar

## Usuario nivel 2 

Este usuario puede:

* Actualizar
* Consultar datos de domicilio

## Usuario nivel 3

Este usuario puede:

* Consultar datos generales

# Resumen

El proyecto consta de 3 microservicios y 2 herramientas

El servicio de registros en donde se introduce el crud del ejercicio
El servicio de usuarios que permite registrar cuentas con privilegios 
El servicio de autenticación, permite generar el token con el que se prodran usar las apis

Idealmente este token tiene un tiempo de vida y permite reconocer la actividad de los usuarios
