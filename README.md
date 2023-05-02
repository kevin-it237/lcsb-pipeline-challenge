# Pipeline Technical Challenge

## Overview
Pipeline that ingests N files, find the maximum and minimum values of each, and output a file with these extrema (a 2-column CSV file).

`Python version: 3.+`


## Run the code locally

```
pip install -r requirements.txt
python pipeline.py
```


## Run the test case
```
python3 -m unittest test_pipeline.py
```


## Run the docker container

The docker configuration is located inside the `Dockerfile`.

1. Build the image

```
docker build -t pipeline-image .
```

Or pull the docker image from docker hub

```
docker pull abelkevin/python-pipeline:latest
```

2. Run the image

```
docker run -v ~/pipeline-data:/app/pipeline-data --name data-pipeline pipeline-image
```

A volume is mounted such that the inputs and the output files are located on the host machine instead of the container.

The pipeline data (inputs and output files) is located in the user's folder of the host machine: `~/pipeline-data`.

----
**To check the output:**

```
cd ~/pipeline-data
cat output.csv
``
----

## Deployment with Github Actions

The image is deployed on `docker hub` after every push on the *master* branch using github actions.

Jobs:

1. Run test cases
2. Deploy docker image

The configuration file is the following:

```yml
name: Publish Docker image

on:
  push:
    branches: ["master"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Check out the repo
      uses: actions/checkout@v3
      
    - name: Log in to Docker Hub
      env:
        DOCKER_USER: ${{ secrets.DOCKER_USER }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
      run: |
        docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
    - name: Docker Build
      run: |
        docker build . --file Dockerfile --tag python-pipeline:latest
    - name: Docker Push
      run: |
        docker tag python-pipeline:latest ${{secrets.DOCKER_USER}}/python-pipeline:latest
        docker push ${{ secrets.DOCKER_USER }}/python-pipeline:latest

```

## Briefly describe what you would need to change for `N=1e6`

We can parallelize the processing of the files across multiple machines.
It is possible by running multiple containers with kubernetes.

We can also use a distributed computing framework like Apache Spark.
It is fast for these kind of tasks.