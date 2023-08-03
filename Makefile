.PHONY: run-app tests install finish-app

run-app:
	docker-compose up -d
finish-app:
	docker-compose down --volumes

tests:
	python -m unittest tests/*.py

install:
	python3 -m venv myenv
	chmod +x ./myenv/bin/activate
	./myenv/bin/activate
	pip install -r requirements.txt
