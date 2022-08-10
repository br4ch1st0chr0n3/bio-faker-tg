export TOP_SERVER=updater
docker compose build
docker compose run create_session
# run a container in detached mode (in background)
docker compose up $TOP_SERVER
# listen to logs
docker compose logs -f $TOP_SERVER