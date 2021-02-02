TOOL = python manage.py

run:
	@$(TOOL) runserver

migrate:
	@$(TOOL) makemigrations
	@$(TOOL) migrate

check:
	@$(TOOL) check

test:
	@$(TOOL) test

collect:
	@$(TOOL) collectstatic --no-input