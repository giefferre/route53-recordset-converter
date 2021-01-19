.PHONY: setup
setup:
	virtualenv -p `which python3` .venv
	( \
		. .venv/bin/activate; \
		pip install -r requirements.txt; \
	)
