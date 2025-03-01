# Pre-requisites
1. Clone repository to local machine
```code
git clone https://github.com/cheahds/KiraTech_Assesment.git
```
2. Ensure that Python version = 3.10.xx is installed
3. Create Virtual environment on the same directory as the repository cloned on the local machine
```code
python -m venv venv
```
4. activate virtual environment
```code
venv\scripts\activate
```
5. Install depedencies by running on the same directory as the repository cloned on the local machine

```code
pip install -r requirements.txt
```

# Runinng Unit Test
```code
cd Inventory_Management
python manage.py runserver
pytest
```
ensure that the server is started before running the unittest

# Running server
```
cd Inventory_Management
python manage.py runserver --insecure
```
Running insecure to load the .css files since debug mode is turned offed

Example URLS:

1. http://localhost:8000/inventory/
2. http://localhost:8000/inventory/?name=item%201
3. http://localhost:8000/inventory/1



# API Endpoints
Some example usage of API endpoints
```
http://localhost:8000/api/inventory
http://localhost:8000/api/inventory/?name=1
```

# Notes
1. .env file is intentionally included into the repo for ease
2. Tested on windows environment
3. Broken image place holder is intentional 