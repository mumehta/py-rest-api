# A simple python, flask, mysql, restapi, swagger app  

By no means this is a best practices example application. It does basic plumbing to get the tasks done. This application is a python restapi application which utlises the power of swagger to fetch data from open web service which return some json data. It can store data to local file and also to mysql database.

## What it does  

Refer `swagger.yml` for restapi calls  

1. Shows user information from  <a href="https://my-json-server.typicode.com/mumehta/py-rest-api">py-rest-api</a> in homepage `http://localhost:9000`

2. `http://localhost:9000/api/get-people-web` reads <a href="https://my-json-server.typicode.com/mumehta/py-rest-api">py-rest-api</a> and stores json data to a local file `data.json`  

3. `http://localhost:9000/api/get-people-file` reads from local `data.json`

4. `http://localhost:9000/api/save-people-db` reads local `data.json` and inserts in mysql


# Pre requisites
1. Make Galera cluster up and running, Ref https://github.com/mumehta/eth-stack
2. Create database by connecting to one of the endpoint, Ref eth-stack
3. Create database person and exit

```
 create table person (id int(10) primary key not null auto_increment, fname varchar(255), lname varchar(255));
```
# Build and run

1. Make virtual env

`python -m venv .venv`

2. `pip install -r requirements.txt`

2. `python app.py`

3. Open browser and make use of endpoint mentioned above

