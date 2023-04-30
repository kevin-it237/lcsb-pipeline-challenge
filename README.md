# Pipeline Technical Challenge

## Overview
Pipeline that ingests N files, find the maximum and minimum values of each, and output a file with these extrema (i.e., a 2-column CSV file).

Python version: 3.+


## Run the code locally

```pip install -r requirements.txt```
```python pipeline.py```


## Run the test case
```python3 -m unittest test_pipeline.py```


## Run the docker container
1. Build the image

```docker build -t pipeline-image .```

2. Run the image

```docker run -v ~/pipeline-data:/app/pipeline-data --name data-pipeline pipeline-image```

A volume is mounted such that the inputs and the output files are located on the host machine instead of the container.

The pipeline data (inputs and the output file) is located in the user folder of the host machine: `~/pipeline-data`.


## Deployment with Github Actions