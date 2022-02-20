docker build -t user_analytics .
docker tag user_analytics <docker_repo>/user_analytics
docker push <docker_repo>/user_analytics