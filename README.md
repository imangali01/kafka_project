# FastAPI + KAFKA


run kafka kafdrop(kafkaui) zookeper<br>
`docker-compose -f kafka/docker-compose.yaml up`

stop kafka kafdrop(kafkaui) zookeper<br>
`docker-compose -f kafka/docker-compose.yaml down -v`

service run command<br>
`uvicorn cmd.run:app --host localhost --port 8000 --reload`

test<br>
`python tests/stress_test.py`