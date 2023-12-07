# SE-technical-challenge
Esta es una aplicación Flask (python) que se ejecuta conectada a una instancia de base de datos postgreSQL con datos predefinidos. Ambos se ejecutan en contenedores docker.
A partir de este código fuente, puede crear la imagen con Docker Compose.
## Reto técnico
Nuestro desafío técnico intenta emular los casos típicos que usted como ingeniero de soporte enfrentará.
1- Recibiste un mensaje de una persona del equipo de Go To Market que supervisa la operación de las Tiendas. Necesitan una información de nuestra base de datos y tú podrías ayudar a esta persona a tenerla haciendo una consulta allí. La persona solicitó una lista de todas las etiquetas que usamos actualmente y cuántas tiendas usan cada etiqueta.
Cree una consulta que le permita proporcionar esta información al equipo de Go To Market.

2- Acabamos de recibir un caso en el que el propietario de la tienda con el id 0d4f7a40-651d-44fb-8744-04d9b31ef844 cambió a Old-Wolf. También dejaron de vender cosas relacionadas con finanzas y ahora están trabajando con educación por lo que también requirieron un cambio en sus etiquetas actuales. Dado que esto es urgente, lo haremos mediante una consulta.
Crear una consulta que nos permita hacer esta actualización en nuestra base de datos.

3- Dado que estamos teniendo dificultades para crear todas las credenciales de la tienda manualmente a través de consultas de inserción, recientemente recibimos un mensaje de un ingeniero de software que creó una API que le permitirá crear nuevas tiendas rápidamente. Actualmente no tenemos un sistema integrado a través de esta API, pero podemos usarlo ahora mismo.
Cree una solicitud HTTP para agregar las credenciales de la tienda a través de nuestra API. El id de la tienda es 1f585fc9-4926-468c-a728-eb34d80e9ea1

---
Dado que las credenciales utilizadas para comunicarnos con nuestro socio son información sensible, se debe realizar un proceso de encriptación. Este proceso se puede realizar realizando una solicitud HTTP a nuestra API que recibe los datos necesarios y agrega las credenciales en la tabla de tiendas. La documentación del punto final se puede encontrar adjunta a este archivo.

---

Las credenciales a sumar para este nuevo aliado son:
```
nombre de usuario: aliado_addi
contraseña: }sxh7_5}BdJ4K:Qf
```

4- Después de un tiempo, la gente empezó a quejarse de que sus credenciales no funcionan. Probablemente algo sucedió mientras otros ingenieros de soporte también usaban esta API. Tienes acceso al registro del servidor que tiene todas las solicitudes anteriores. Debe abrir el registro dentro de la carpeta log/example.log y encontrar cuántas solicitudes fallaron y cuáles son los clientes que se vieron afectados.

5- Cree los runbooks en el archivo Léame relacionados con esos casos.

### Consideraciones técnicas:
* Esperamos que ejecute la aplicación en la máquina local usando Docker
* Esperamos que cree consultas SQL utilizando funciones de manejo de datos json. Puede utilizar herramientas de gestión de bases de datos como DBeaver
* Puede utilizar cualquier herramienta o lenguaje de programación para realizar solicitudes HTTP a la API. Por ejemplo Postman, CURL, wget o cualquier lenguaje de programación.
* Esperamos un archivo README que describa el proceso general y los pasos para desarrollarlo utilizando los recursos creados durante el proceso (consultas, solicitudes de API, inspección de registros). El objetivo de ese README es ser utilizado como referencia futura para que otras personas puedan seguir los mismos pasos y lograr el mismo resultado. Por eso el documento debe ser claro y autoexplicativo.
* No esperamos que publique la aplicación en la Internet pública.

### Entregables:
- Script SQL para listar la distribución de las tiendas por etiquetas según el ítem 1
- Consulta SQL para actualizar información de la tienda según el ítem 2
- Solicitud HTTP que agrega las credenciales de un determinado aliado a través de nuestra API según el ítem 3
- Cuáles fueron los aliados afectados por el problema mencionado en el punto 4 y una posible solución para esos casos.
- Un README a modo de runbook explicando cómo realizar esos 4 procesos.
- Esperamos recibir estos archivos en un repositorio privado de GITHUB.

## ¿Cómo iniciar la aplicación en entorno local?
Para correr esta aplicación en un entorno local se deben cumplir los siguientes requisitos:

- Usar un entorno Linux (Distribuciones como Ubuntu o Manjaro son las más populares)
- Tener instalado docker
- Tener instalado Git

Luego se deben realizar los siguientes pasos:

1. Clonar este repositorio en una carpeta local.
```bash
git clone https://github.com/AdelanteFinancialHoldings/SE-technical-challenge.git
```
2. Dentro de la carpeta clonada, ejecute el siguiente comando:
```bash
docker compose build
```
3. Ejecute las imágenes ejecutando el siguiente comando:
```bash
docker compose up
```

Esto inicia la aplicación y la base de datos, que escuchan en los puertos 4000 y 5432 respectivamente. No cierres la terminal porque el registro que se muestra allí es importante para un paso específico del desafío.

Para detener la aplicación en cualquier momento ejecute CTRL + C
### Cómo conectarse a la base de datos
Las credenciales para la base de datos implementada localmente son:
```
- anfitrión: localhost: 5432
- base de datos: postgres
- contraseña: postgres
```

## Especificación de los endpoint de la API:
La api al iniciarse con el comando run_flash.sh realiza lo siguiente:
- Iniciar la aplicación.
- Poblar la base de datos con datos aleatorios.
- Empieza a escuchar requests en la dirección 127.0.0.1:4000
### Endpoint: credentials
```
POST /allies/{allyId}/credentials
Add communication credentials to an ally

Headers: "Content-Type: application/json"

Parameters:
allyId(path): string identification for an ally.

Payload(body): json object, example
{
	"user": "addi",
	"password": "123456"
}

Responses:
200: 
{
	"message": "Credentials added",
	"allyId": "allyId",
	"allyName": "ally name"
}
400:
{
	"message": "The ally was not found or the request is not correct"
}
500:
{
	"message": "Server error"
}
```

```
GET /allies/{allyId}/credentials

Checks if the given ally has active credentials and is an allowed origin in our application

Headers: "Content-Type: application/json"

Parameters:
allyId(path): string identification for an ally.

Responses:
200: 
{
	"message": "Ally has credentials set!"
}
400:
{
	"message": "Ally does not have credentials set!"
}
404:
{
	"message": "Ally was not found"
}
500:
{
	"message": "Server error"
}
```
