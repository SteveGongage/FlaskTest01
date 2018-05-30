# NOTHING TO SEE HERE...

Move along people... this is a test project of no consequence.  

## Links used for this demo ...


[Resful APIs with Flask](https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx)

[Setting up PostreSQL on Cloud 9](https://community.c9.io/t/setting-up-postgresql/1573)

[Getting started with Flask on Cloud 9](https://damyanon.net/post/getting-started-with-flask-on-cloud9/)

[First Endpoint Here](https://flask-test-app-captainsteve.c9users.io/api/Hello)


# Useful commands

## PostreSQL Commands

### Running the Server

Start the PostreSQL service

`sudo service postgresql start`

Connect via the command line

`psql` or `psql database_name`

Create a PostgreSQL database

`CREATE DATABASE "tablename"`

Using the Command Line

`\c testflask` to connect to the database.

Then you can use normal SQL like `SELECT * FROM categories` to query the connected database

### Initial Setup

List databases

`\list`

Setting a Database - where 'postgres' is the username

`password postgres`

### Migrations
Initialize the migrations by using the 'init' command.  This will create the directories and setup files needed.  Only needed the first time.

`python migrate.py db init`

Create the migration by running the 'migrate' command.  

`python migrate.py db migrate`

Apply the migrate by running the 'upgrade' command

`python migrate.py db upgrade`

# Other Resources

* [Setting up GitHub for Cloud9](http://lepidllama.net/blog/how-to-push-an-existing-cloud9-project-to-github/)
* 