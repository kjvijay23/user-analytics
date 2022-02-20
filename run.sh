docker run -d -p 5000:5000 -e GOOGLE_APPLICATION_CREDENTIALS=/app/config.json --name user-analytics user_analytics
docker logs user-analytics --follow
docker rm user-analytics -f
echo -e "\n"
read -p 'Press enter to exit'