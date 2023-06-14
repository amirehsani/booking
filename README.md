# booking
Sample back-end project representing a platform with capability of booking resorts and flight tickets. All the tech and tools that are used in this project:

Python -> main language
Django -> main back-end framework
DRF -> creating APIs, managing request/response cycles.

PostgreSQL -> main database
Redis -> main caching data storage - secondary database

Docker -> containerizing the project
Swagger -> API documentation

see more in requirements.txt

## project setup

1- Complete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd booking
```

2- Setup venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- Install dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- Create an env
```
cp .env.example .env
```

5- Create tables
```
python manage.py migrate
```

6- Spin off Docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

7- Run the project
```
python manage.py runserver
```