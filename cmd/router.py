import json

from fastapi import APIRouter
from aiokafka import AIOKafkaProducer

from cmd import config, schema
from cmd.shared import loop


route = APIRouter()


@route.post('/create_message')
async def send(message: schema.Message):
    producer = AIOKafkaProducer(
        loop=loop,
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS
    )

    await producer.start()

    try:
        print(f'Sendding message with value: {message}')
        value_json = json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=config.KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()
