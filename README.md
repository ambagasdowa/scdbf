# scdbf

Simple cat dbf files written in python

Testing in ![Ranger FM](https://github.com/ranger/ranger "Ranger FileManager") as viewver

Add in scope.sh

```sh
# ...
#file scope.sh

#dbf view

	dbf)
		scdbf "${FILE_PATH}" && exit 5
		exit 1;;

```

![Ranger FM](./screenshots/ranger_dbf.png "Ranger View")

View in ![bat](https://github.com/sharkdp/bat "bat") pager

![Batcat](./screenshots/batcat_pipe.png "Pipe to Batcat")

## Install

```sh
pip install scdbf
```
