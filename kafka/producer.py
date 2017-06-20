import time
from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError
def print_response(response=None):
    if response:
        print('Error: {0}'.format(response[0].error))
        print('Offset: {0}'.format(response[0].offset))
def main():
    kafka = KafkaClient("104.154.244.37:9092")
    producer = SimpleProducer(kafka)
    msg = []
    topic = b'test'
    try:
        with open("/root/kafkaprojects/Iris.csv") as f:
            for msg in f:
                print_response(producer.send_messages(topic,b'msg'))
    except LeaderNotAvailableError:
        # https://github.com/mumrah/kafka-python/issues/249
        time.sleep(1)
        print_response(producer.send_messages(topic, msg))
    kafka.close()
if __name__ == "__main__":
    main()
