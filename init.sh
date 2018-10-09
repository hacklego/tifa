docker-compose start
docker exec -it tifa_db_1 mongo 127.0.0.1/tif --eval 'var document = {name  : "admin" , passwd : "abc123.",}; db.users.insert(document);'
docker-compose restart
sudo docker exec -it tifa_web_1 python3 main.py
