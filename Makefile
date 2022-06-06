init:
	. ./setenv.sh

start:
	poetry run python3 task_manager/manage.py runserver