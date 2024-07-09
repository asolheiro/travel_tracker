make dependencies:
	clear
	@poetry install
	
make dev-server:
	clear
	poetry run python run.py

make test:
	clear
	poetry run pytest -svv