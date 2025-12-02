.PHONY: help install test format lint clean day

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run all tests"
	@echo "  make format     - Format code with black"
	@echo "  make lint       - Lint code with flake8"
	@echo "  make clean      - Remove cache and build files"
	@echo "  make day DAY=N  - Create a new day folder (e.g., make day DAY=5)"

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest -v

format:
	black .

lint:
	flake8

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov/

day:
	@if [ -z "$(DAY)" ]; then \
		echo "Error: Please specify DAY=N (e.g., make day DAY=5)"; \
		exit 1; \
	fi
	python create_day.py $(DAY)
