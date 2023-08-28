## How to run locally

If you want to run this app, you have to setup the environment variable and the mysql database.

## Setup mysql database

Create a user with a password
```text
mysql> CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password123'
mysql> GRANT ALL PRIVILEGES ON note_taking_fast_api.* TO 'user1'@'localhost';
```

Login using the credentials provided
```text
$ mysql -u user1 -p
```

Create a database
```text
mysql> CREATE DATABASE note_taking_fast_api;
```

## Setup environment variable

Create a file .env and write this:
```text
# REST API SERVER
SERVER_IP='localhost'
SERVER_PORT=8000

# MYSQL DATABASE
USERNAME='user1'
PASSWORD='password123'
DATABASE_IP='localhost'
DATABASE_PORT='3306'
DATABASE_NAME='note_taking_fast_api'
TABLE_NAME='notes'
```

## Run the server
```
$ bash start_server.sh
```