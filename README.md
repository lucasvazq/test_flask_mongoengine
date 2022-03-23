# Issue with `flask_mongoengine`

https://github.com/MongoEngine/flask-mongoengine/issues/449

## Below are some simple steps to reproduce this problem.

Prerequisites:
  - Docker.
  - Docker compose.
  - `docker` group created.
  - Our user added to `docker` group.

1 - Clone this repository and access it:
```
git clone git@github.com:lucasvazq/test_flask_mongoengine.git && cd test_flask_mongoengine
```

2 - Run the containers:
```sh
docker-compose build --no-cache && docker-compose up
```

3 - Try to access to:
  - [localhost:5000/test_flask_pymongo/](localhost:5000/test_flask_pymongo/) ✔️
  - [localhost:5000/test_flask_mongoengine/](localhost:5000/test_flask_mongoengine/) ❌
