# AI | Budget Manager

## Usage

Here are some quickstart instructions, although I would look at the [documentation](https://github.com/tko22/flask-boilerplate/wiki) for more details and other options of setting up your environment (e.g. full Docker setup, installed postgres instance, pipenv, etc).

First start a postgres docker container and persist the data with a volume `flask-app-db`:

```
make start_dev_db
```

Another option is to create a postgres instance on a cloud service like elephantsql and connect it to this app. Remember to change the postgres url and don't hard code it in!

Then, start your virtual environment

```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```
Now, install the python dependencies and run the server:
```
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r requirements-dev.txt
(venv) $ python manage.py recreate_db
(venv) $ python manage.py runserver
```

To exit the virtual environment:
```
(venv) $ deactivate
$
```

For ease of setup, I have hard-coded postgres URLs for development and docker configurations. If you are using a separate postgres instance as mentioned above, _do not hardcode_ the postgres url including the credentials to your code. Instead, create a file called `creds.ini` in the same directory level as `manage.py` and write something like this:

```
[pg_creds]
pg_url = postgresql://testusr:password@127.0.0.1:5432/testdb
```
Note: you will need to call `api.core.get_pg_url` in the Config file.

For production, you should do something similar with the flask `SECRET_KEY`.

#### Easier setup

I've created a makefile to make this entire process easier but purposely provided verbose instructions there to show you what is necessary to start this application. To do so:
```
$ make setup
```

If you like to destroy your docker postgres database and start over, run:
```
$ make recreate_db
```
This is under the assumption that you have only set up one postgres container that's linked to the `flask-app-db` volume.

I would highly suggest reading the [documentation](https://github.com/tko22/flask-boilerplate/wiki) for more details on setup.

#### Deployment

You may use Heroku or Zeit Now and the instructions are defined in the [wiki page](https://github.com/tko22/flask-boilerplate/wiki). I would recommend Heroku. The easiest way to do so is to click the Heroku Deploy button. Remember, once you fork/copy this repo, you will need to change `app.json`, especially the `repository` key. Everything else should be fine.

### Repository Contents

- `api/views/` - Holds files that define your endpoints
- `api/models/` - Holds files that defines your database schema
- `api/__init__.py` - What is initially ran when you start your application
- `api/utils.py` - utility functions and classes - explained [here](https://github.com/tko22/flask-boilerplate/wiki/Conventions)
- `api/core.py` - includes core functionality including error handlers and logger
- `api/wsgi.py` - app reference for gunicorn
- `tests/` - Folder holding tests

#### Others

- `config.py` - Provides Configuration for the application. There are two configurations: one for development and one for production using Heroku.
- `manage.py` - Command line interface that allows you to perform common functions with a command
- `requirements.txt` - A list of python package dependencies the application requires
- `runtime.txt` & `Procfile` - configuration for Heroku
- `Dockerfile` - instructions for Docker to build the Flask app
- `docker-compose.yml` - config to setup this Flask app and a Database
- `migrations/` - Holds migration files – doesn't exist until you `python manage.py db init` if you decide to not use docker

### MISC

If you're annoyed by the **pycache** files

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

### Additional Documentation

- [Flask](http://flask.pocoo.org/) - Flask Documentation
- [Flask Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) - great tutorial. Many patterns used here were pulled from there.
- [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - the ORM for the database
- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - Deployment using Heroku
- [Learn Python](https://www.learnpython.org/) - Learning Python3
- [Relational Databases](https://www.ntu.edu.sg/home/ehchua/programming/sql/Relational_Database_Design.html) - Designing a database schema
- [REST API](http://www.restapitutorial.com/lessons/restquicktips.html) - tips on making an API Restful
- [Docker Docs](https://docs.docker.com/get-started/) - Docker docs

Feel free to contact me for questions and contributions are welcome :) <br>
tk2@illinois.edu
