# SE-technical-challenge
This is a Flask (python) application that runs connected to a postgreSQL database instance with pre-defined data. Both are executed in docker containers.
From this source code you can build the docker image using Docker Compose.
## Technical challenge:
Our technical challenge tries to emulate the typical cases that you as a Support Engineer will face.
1- You received a message from a person from the Go To Market team that oversee the Stores operation. They need an information from our database and you could help this person to have it by doing a query there. The person requested a list of all the tags that we currently use and how many stores are using each tag.
Create a query that allow you to provide this information to the Go To Market team.

2- We just received a case where the owner of the store with the id 0d4f7a40-651d-44fb-8744-04d9b31ef844 changed to Old-Wolf. They also stopped to sell things related to finanzas and are now working with educacion so they also required a change in their current tags. Since this is urgent we will do that thru a query.
Create a query that allow us to do this update in  our database.

3- Since we are having a hard time while creating all the store credentials manually thru insert queries we recently received a message from one Software Engineer that build an API that will allow you to create new stores quickly. Currently we don't have system integrated thru this API but we can use it right now.
Build an HTTP request to add the store credentials through our API. The id of the store is 1f585fc9-4926-468c-a728-eb34d80e9ea1

--- 
Since the credentials used to communicate with our partner are sensitive information, an encryption process must be carried out. This process can be done by making an HTTP request to our API which receives the necessary data and adds the credentials in the stores table. Endpoint documentation can be found attached to this file. 

---

The credentials to add for this new ally are:
```
username: aliado_addi
password: }sxh7_5}BdJ4K:Qf
```

4- After some time people started to complain that their credentials are not working. Probably something happened while other Support Engineers were also using this API. You have access to the server log that have all the previous requests. You should open the log inside the folder log/example.log and find how many requests failed and which are the clients that were impacted.

5- Create the runbooks in the readme related to those cases.


### Technical considerations:
* We expect you to run the application on local machine using docker
* We expect you to build SQL queries using json data handling functions. You can use database management tools like DBeaver
* You can use any tool or programming language to perform HTTP resquests to the API. For example Postman, CURL, wget or any programming languages.
* We expec a README file describing the general process and the steps to develop it using the resources created during the process (queries, API requests,Log Inspection). The goal of that README is to be used as future reference so other people can do the same steps and achieve the same result. Because of that the document should be clear and self-explanatory.
* We do not expect you to publish the application on the public internet

### Deliverables:
- SQL script to list the distrubution of the stores by the tags according to the item 1
- SQL query to update store information according to the item 2
- HTTP Request that adds a given ally's credentials through our API according to the item 3
- Which were the allies affected by the issue mentioned on the item 4 and a possible solution for those cases
- A README as a runbook explaining how to carry out those 4 processes.
- We hope to receive these files in a private GITHUB repository.

## How to run this app in local environment?
To run this application in a local environment, the following requirements must be met:

- Use a Linux environment (Distributions like Ubuntu or Manjaro are the most popular)
- Have docker installed
- Have docker compose installed
- Have Git installed   

Then the following steps must be performed:

1. Clone this repository to a local folder.

```bash
git clone https://github.com/AdelanteFinancialHoldings/SE-technical-challenge.git
```
2. Inside the recently cloned folder run the following command
```bash
docker compose build
```
3. Then execute the images by typing the following command
```bash
docker compose up
```

This starts the application and the database, which are listening on port 4000 and 5432 respectively. Don't close the terminal because the log shown there is important for an specific step of the challenge.

To stop the application anytime run CTRL + C
### How to connect to the database
The credentials for the locally deployed database are:
```
- host: localhost:5432
- database: postgres
- password: postgres
```

## API endpoint specification:
- The application starts after the database is populated with data.
- It keeps listening requests at address 127.0.0.1:4000

### Endpoint: credentials
```
POST /allies/{allyId}/credentials
Add communication credentials to an ally

Headers: "Content-Type: application/json"

Parameters:
allyId(path): string identification for an ally.

Payload(body): json object, example
{
	"username": "addi",
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
