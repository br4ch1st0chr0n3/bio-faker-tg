export TOP_SERVER=updater
docker compose build
# run a container in detached mode (in background)
docker compose up -d $TOP_SERVER
# listen to logs
docker compose logs -f $TOP_SERVER

echo "wtf"