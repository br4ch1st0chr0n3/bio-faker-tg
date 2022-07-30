export CONTAINER_NAME=updater
docker compose build
# establish a session with Telegram
docker compose run create_session
# run a container in detached mode (in background)
docker compose up -d $CONTAINER_NAME
# listen to logs
docker compose logs -f $CONTAINER_NAME