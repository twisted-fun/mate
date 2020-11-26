help:
	@echo ""
	@echo "Available commands"
	@echo ""
	@echo " - install      : installs mate as bash command"
	@echo " - flake        : runs flake8 style checks"
	@echo " - check        : runs all checks (tests + style)"
	@echo " - clean        : cleans up all folders"
	@echo ""

install:
	pip install -e .

flake:
	flake8

test:
	pytest

clean:
	rm -rf __pycache__ .pytest_cache

check: flake test clean
