# Serverless Python Gitlab CI Boilerplate

Serverless backend for the website

## Configuring CI/CD

You need to build the docker image if you don't want to use the default

- check the registry tab in the project on GitLab for instructions

Requires environmental variables from IAM user created for deployments:

- AWS_ACCESS_KEY_ID with the new user’s access key
- AWS_SECRET_ACCESS_KEY with the new user’s access secret key

## Recommendations

- Disable committing to master and only allow changes by merging via branches

## Dev Javascript (Serverless related)

Install

```bash
yarn install
```

Run linting and auto correct errors

```bash
yarn lint
```

## Dev Python

Install

```bash
python3 -m venv  venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r dev-requirements.txt
```

Lint

```bash
pylint src
pylint tests
pylint e2e
```

Run unit tests

```bash
pytest tests
```

Run End to End tests

```bash
pytest e2e
```

## Docker image

Docker image with python, nodesjs and serverless is required.
