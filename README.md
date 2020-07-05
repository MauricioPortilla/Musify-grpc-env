# Musify-grpc-env
Servidor de procesamiento gRPC en Docker para Musify.

![Musify-grpc-env CI](https://github.com/MauricioPortilla/Musify-grpc-env/workflows/Musify-grpc-env%20CI/badge.svg?branch=master)

## Contribuidores
- Cruz Portilla Mauricio
- Romero Peña Arturo Iván

## Requerimientos
- Docker
- Docker compose

## Instrucciones de ejecución
1. En una terminal, moverse al interior de la carpeta de este proyecto.
2. Ejecutar: `$ docker network create --driver bridge --subnet 172.250.6.0/24 musify_network` para crear la red entre los servidores.
3. Ejecutar: `$ docker-compose build`.
4. Ejecutar: `$ docker-compose up -d` para levantar el contenedor en segundo plano.

Una vez realizado esto, el servidor estará listo para su utilización.

### Servidores
- <a href="https://github.com/MauricioPortilla/Musify-dev-env">Musify-dev-env</a>: Servidor de API REST.
- <a href="https://github.com/MauricioPortilla/Musify-db-env">Musify-db-env</a>: Servidor de Base de datos.

### Cliente
- <a href="https://github.com/MauricioPortilla/Musify">Musify</a>: Cliente de escritorio
- <a href="https://github.com/MauricioPortilla/MusifyMobile">MusifyMobile</a>: Cliente móvil
