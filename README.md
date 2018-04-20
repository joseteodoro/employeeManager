# Employees Manager Project

This project uses DJango and Django-Rest-Framework to build a Employees Manager with admin site and Rest integrations.

## Installing and running

The project is configured to run inside `docker` or inside virtual environment.
For docker use:

```bash
cd 'PATH_TO_PROJECT'
docker build . --tag employeeManager:lastest
docker run -p 8000:8000 employeeManager:v1
```

The Django server will startup on the port `8000` and Docker will expose that for you.

The Django secretKey is being passed by environment variable. So, you can pass it to docker using the command:
```bash
docker run -e SECRET_KEY your_secret_key employeeManager:lastest
```

For virtual env usage:

```bash
cd 'PATH_TO_PROJECT'
source ./bin/activate
export SECRET_KEY=your_secret_key
pip install --no-cache-dir -r requirements.txt
python manage.py migrate
python manage.py runserver
``` 

## The web interface

After start the Django, you can use the browser to go to `http://0.0.0.0:8000/` and take a look on the availables APIs:

```json
{
    "employee": "http://0.0.0.0:8000/employee/",
    "department": "http://0.0.0.0:8000/department/"
}
```

Without loging, you can list the records, but you can only POST and DELETE data after authenticated or passing the user and password when using some terminal command like `curl`.
To login first time, connect to the docker using the Django command: `createsuperuser`.

Go to the project folder if you are running locally, or inside docker if you are running on docker:

For docker
```bash
instance_id=$(docker ps | grep employeeManager | awk '{print $1;}')
docker exec -it $instance_id /bin/bash
python manage.py createsuperuser
```

You will be asked about the username and password.

For Django running locally:
```bash
cd path_to_project
python manage.py createsuperuser
```

## Database

The database is normalized, so you must pass a reference for `Department` instead of pass only its name.
I decided to use the linked reference to improve navigability.
So, when posting a new employee please use the form:

```bash
{
        "name": "Jose Teodoro da Silva",
        "email": "josets@br.ibm.com",
        "department": "http://0.0.0.0:8000/department/1/"
    }
```

Where `"http://0.0.0.0:8000/department/1/"` is the full path to the department record.
These records are also integrated with the Django Admin page.

The project is using SQLite to simplify the solution. To make the database persistent, please use docker volumes when starting the image:

```bash
docker run -p 8000:8000 -v local_path_to_your_data
 :/data/db.sqlite3 employeeManager:v1
```