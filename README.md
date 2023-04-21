# text-image-conversion-tool

## How to install this repo
1. build a python virtual env with python=3.10
```shell
conda create --name venv python=3.10
```
2. activate the venv and install packages
```shell
conda activate venv
pip install -r requirements.txt
```
3. intsall pre-commit
```shell
pre-commit install
```

## Useful Command
build docker image
```shell
make build
```
open a shell in docker
```shell
make shell
```
run the service on localhost:8000 (via docker)
```shell
make local-web-start
```
stop the service on localhost:8000 (via docker)
```shell
make local-web-stop
```
deploy the service on localhost:8000 (via scripts)
```shell
make local-deploy
```
