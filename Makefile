build:
	python -m build
install:
	pip install dist/
uninstall:
	pip uninstall -y env2cli
publish:
	twine upload dist/*.tar.gz
clean:
	rm -rf build dist