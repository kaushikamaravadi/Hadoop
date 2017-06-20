from kafka import KafkaClient, SimpleConsumer
kafka_client = KafkaClient("104.154.244.37:9092")
consumer = SimpleConsumer(kafka_client, b"hello_group_consumer", b"test")
for message in consumer:
        # This will wait and print messages as they become available
    print(message)
if __name_
