export DOCKER_BUILDKIT=1
docker compose build
docker compose run create_session
docker compose up updater