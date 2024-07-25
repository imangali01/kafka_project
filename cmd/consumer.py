import asyncio
import random

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from cmd import config
from cmd.shared import loop



async def consume():
    consumer = AIOKafkaConsumer(
        config.KAFKA_TOPIC,
        loop=loop,
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        group_id=config.KAFKA_CONSUMER_GROUP
    )

    await consumer.start()

    try:
        async for msg in consumer:
            print(f'Consumer msg: {msg}')
            await asyncio.sleep(random.uniform(0.1, 1.5))
    finally:
        await consumer.stop()
