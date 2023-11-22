## T3 Hadoop MapReduce

## Cómo correr el contenedor

Para poder levantar el contenedor:

	docker build -t hadoop . 
	docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop

Podemos ver si el contenedor está listo para correr viendo si se levantó la interfaz gráfica de Hadoop:

`curl 'http://localhost:9870/dfshealth.html#tab-overview' | grep 'active'`

## Cómo entrar al contenedor

	docker exec -it hadoop bash

## Qué hacer antes de levantar código
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input

## Cómo probar el código

	cat data.txt | python mapper.py | sort -k1,1 | python reducer.py

---

Pasamos el input al hdfs;
	`hdfs dfs -put data-text.txt input`

## Cómo levantar código
Hacemos lo siguiente en el directorio donde se encuentran los archivos:

	mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py

Dado que específicamos que el output se guardara en  `/user/hduser/output`, podemos ver la salida del Job :
	`hdfs dfs -cat /user/hduser/output/*`
