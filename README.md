# SE-technical-challenge
Esta es una aplicación de Flask (python) que corre junto a una base de datos de postgreSQL con datos aleatorios en un contenedor docker.
A partir de este código fuente se puede construir la imagen docker.
## Reto técnico
Nuestro equipo de ventas le ha pedido a nuestro equipo de ingeniería de soporte la configuración de un proceso pre-establecido para integrar un nuevo aliado a nuestra plataforma. Este proceso requiere añadir nuevos registros a una base de datos SQL y usar un endpoint de nuestra plataforma.   

El proceso consiste de:  

Se necesita construir un script SQL que permita agregar una nueva fila a la tabla "stores". Se debe también construir un script SQL que permita consultar los datos de un aliado dado cierto id

 - Datos:
  1. id: 1234567890
  2. name: Aliado ADDI
  3. tags: Tecnología, información, finanzas
  4. brand: Merchant
  5. descuento: 5
  6. Monto máximo: 150
  7. Monto mínimo: 20
  8. credentials: null

Dado que las credenciales usadas para la comunicación con nuestro aliado son información sensible, se debe realizar un proceso de encriptación de las mismas. Este proceso se puede realizar haciendo una request HTTP a nuestra API la cual recibe los datos necesarios y agrega las credenciales en la tabla de stores. La documentación de los endpoints se puede encontrar adjunto a este archivo.

Se deberá crear el código necesario para realizar una request HTTP que sea reutilizable y permita cambiar los parámetros de la request a necesidad. Puede usar cualquier lenguaje de programación, herramientas de línea de comandos como wget y curl ó herramientas gráficas como postman generando un archivo de collección de postman.
 - Las credenciales a añadir para este nuevo aliado son:
  1. username: aliado_addi
  2. password: }sxh7_5}BdJ4K:Qf

### Consideraciones técnicas:
* Se espera que corra la aplicación en máquina local usando docker
* Esperamos que construya queries SQL utilizando las funciones de manejo de datos json. Puede usar herramientas de gestión de bases de datos como DBeaver
* Puede usar cualquier herramienta o lenguaje de programación para realizar resquests HTTP a la API. Por ejemplo Postman, CURL, wget o lenguajes de programación.
* Esperamos un archivo README describiendo el proceso general y los pasos para desarrollarlo usando los recursos creados durante el proceso (queries, requests a API). Esto con la idea de que sea usado para futura referencia y que sea un documento fácil de seguir por otra persona.
* No esperamos que publiques la aplicación en el internet público
  
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
2. Construir la imagen docker (Con una terminal en el directorio que contiene la dockerfile):
```bash
sudo docker build -t addi-assesment .  
```
3. Correr el archivo de bash "run.sh":
```bash
bash run.sh  
```
4. Abrir el bash del contenedor dockerOpen the docker's bash:  
```bash
sudo docker exec -it addi-app /bin/bash  
```
* Alternativamente se puede usar el archivo con nombre amigable:  
```bash
bash enter_docker_bash.sh  
```
5. Una vez dentro del cli del docker, se estará en una carpeta que contiene el scrip necesario para iniciar la aplicación "run_flask.sh":  
```bash
bash run_flask.sh  
```

Esto inicia la aplicación y la base de datos, los cuales están escuchando el puerto 5000 y 5432 respectivamente. A este punto se puede cerrar la terminal y continuará ejecutándose la aplicación.

Para detener la aplicación se puede usar desde una terminal diferente: 
```bash
sudo docker stop addi-app
sudo docker system prune
```


## Especificación de los endpoint de la API:
La api al iniciarse con el comando run_flash.sh realiza lo siguiente:
- Iniciar la aplicación.
- Poblar la base de datos con datos aleatorios.
- Empieza a escuchar requests en la dirección 127.0.0.1:5000
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
