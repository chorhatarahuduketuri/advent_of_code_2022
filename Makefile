format:
	black .

lint:
	flake8 .

quality: format lint

test:
	pytest