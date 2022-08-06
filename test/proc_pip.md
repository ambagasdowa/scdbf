#build app

##update version

```sh
	python3 -m build
```

> upload to repo

```sh
	python3 -m twine upload --verbose --skip-existing github/scdbf/dist/*
```
