export CONTAINER_NAME=updater
docker compose build
docker compose run create_session
docker compose up -d $CONTAINER_NAME
docker compose logs -f $CONTAINER_NAME