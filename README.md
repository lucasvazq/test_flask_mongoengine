# Issue with `flask_mongoengine`

Trace it at: ...

## Below are some simple steps to reproduce this problem.

Prerequisites:
  - Docker.
  - Docker compose.
  - `docker` group created.
  - Our user added to `docker` group.

1 - Clone this repository
```
git clone git@github.com:lucasvazq/test_flask_mongoengine.git
```

2 - Run the flask app
```sh
docker-compose build --no-cache && docker-compose up
```

3 - Try to access to:
  - [localhost:5000/test_flask_pymongo/](localhost:5000/test_flask_pymongo/) ✔️
  - [localhost:5000/test_flask_mongoengine/](localhost:5000/test_flask_mongoengine/) ❌
