# Installation

First, create a virtual environment for the project
```
python -m virtualenv -p python3 .virtualenv
source .virtualenv/bin/activate 
```
then install the dependencies
```
pip install -r requirements.txt
```

# Unittests

After installation is complete, it is good to run the unittests:
 ```
 make test
 ```

# Running the server

There are two ways to run the development server:
```
make devserver
```
or you can manually set `PYTHONPATH` and `DJANGO_SETTINGS_MODULE` environment
variables and then run django's `manage.py`:
```
export PYTHONPATH=$PYTHONPATH:$(pwd)/kriegspiel_api_server
export DJANGO_SETTINGS_MODULE=settings.base
kriegspiel_api_server/manage.py runserver
```