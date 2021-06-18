# literate-guide - travel the pipe

This repo is not a fully running application, but with the structure set up ready for further implementation.

There are three main modules integrated, each serves different purposes:
* `jsonschema` validates a json data against the affirmed schema
* `SQLAlchemy` creates a session as the intermedium to perform database execution
* `great-expectations` does checks against dataset as monitoring tool

## Get started

As shown in [Dockerfile](ops/Dockerfile), [main.py](src/main.py) is the entrypoint and [temp](temp/) folder will be attached as volume to the container.

Put the source file into temp folder, as of now the file name needs to be `sample_data.json` but later on it can be passed as a parameter in the command.

The file will be read line by line for validation and database insertion.
## Validation

In [validate.py](src/utils/validate.py), there are two steps of validation:
* Check if the string line is a valid json string
* Check if the json data complies the json schema

Some future works regarding to schema change/evolution:
* Set up a schema repository, check the following during validation
    * whether the current schema already existed in repo, and if it does, verify that they are identical, otherwise push it to the repo
    * whether the changes between the predecessor of the schema and the current version are backwards compatible

## Database operation

Load each record to a stage table as we can process some quality checks before loading to final table.

In order to load the sample data into Postgres/MySQL database, the data structure is flattented and each subfield inside `data` field becomes a column of the table. Since I'm not familiar with event-driven architecture, I might disregard the best practice to load such data into such database.

Insert the data of stage table into final table after checking the quality is as expected.

## Monitoring

In [monitor.py](src/utils/monitor.py), great_expectations module is introduced to perform data quality checks:
* As the source file being read through, a simple counter is used to count the amount of valid rows. The count is used as the expected row count of stage table.
* For future works, great_expectations can be used as a profiling tool against the final table. It gives us an overview of the dataset, such as percentage of each event on a daily basis or if there's any anomaly in some specific events after comparing to.

## CI/CD
As shown in [ci.yaml](ops/ci.yaml), there can be 3 stages in the development pipeline:
* master: build the docker image and publish it to docker repo
* staging: automatically deploy the service to qa environment after master stage succeeds
* prod: only can manually deploy the service to prod environment after staging stage succeeds

In order to deploy the service to Kubernetes, there can be a repo server set up which hosts Kubernetes manifest yaml files.
```
kubectl apply -f "$(KUBERNETES_MANIFEST_YAML_REPO_URL)/$(PROJECT_NAME)?env=$(APP_ENV)"
```
This command will be executed upon each deployment based on the `PROJECT_NAME` and `APP_ENV`. `APP_ENV` is the environment variable fetched from CI server, so the service can be deployed to the corresponding cluster.
