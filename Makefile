.PHONY: run-app tests install finish-app clean

# Default target
run: run-app

run-app:
	@echo "Starting the application..."
	docker-compose up -d
	@echo "Application is up and running!"

finish-app:
	@echo "Stopping the application..."
	docker-compose down --volumes
	@echo "Application stopped successfully."

tests:
	@echo "Running tests..."
	pytest

# Target for setting up the virtual environment
install:
	@echo "Setting up the virtual environment..."
	python3 -m venv myenv
	@echo "Virtual environment created."
	@echo "Installing dependencies..."
	source myenv/bin/activate && pip install -r requirements.txt
	@echo "Dependencies installed successfully."

# Target for cleaning up temporary files or compiled code
clean:
	@echo "Cleaning up temporary files..."
	rm -rf __pycache__  # Remove Python
