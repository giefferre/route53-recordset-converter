.PHONY: clean
clean:
	rm -rf build dist

.PHONY: build
build: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*
