## T3 Hadoop MapReduce
	En la carpeta T3-SD-HADOOP
	docker build -t hadoop . 
	docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
	docker exec -it hadoop bash

## Dentro del contenedor
	hdfs dfs -mkdir /user
	hdfs dfs -mkdir /user/hduser
	hdfs dfs -mkdir input
	sudo chown -R hduser .

## Probar en un solo .txt
	cd examples/
	cat 1/1.txt | python mapper.py 	# Para ver los output del mapper
	cat 1/1.txt | python mapper.py| sort -k1,1 | python reducer.py	# Para ver los output del mapper y reducer

## Pasamos el input al hdfs
	hdfs dfs -put text.txt input
	-Desde el 1/1.txt al 2/30.txt-
	No hice código que lo haga automáticamente, pero gracias al nombre de 
	las carpetas y archivos no es tan tedioso

## Código streaming
	mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py

## Al finalizar el código, es útil traer los datos del output, usando los siguientes comandos
	hdfs dfs -get /user/hduser/output/ /home/hduser/examples # Trae la carpeta output a la carpeta examples
	exit	# Salimos del hdfs
	docker cp hadoop:/home/hduser/examples/output examples # Traemos la carpeta desde hadoop a nuestro ambiente de código

## Pasar datos a JSON
	python tojson.py
	node app.js
	
	Usar postman con
	http://localhost:3000/top5documents?name=externos