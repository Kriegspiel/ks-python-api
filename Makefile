export PYTHONPATH:=${PYTHONPATH}:$(shell pwd)/kriegspiel_api_server
export DJANGO_SETTINGS_MODULE:=settings.base
echo:
	echo $(PYTHONPATH)
test:
	pytest tests
devserver:
	python kriegspiel_api_server/manage.py runserver