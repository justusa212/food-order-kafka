from kafka import KafkaConsumer

consumer = KafkaConsumer('order_details', bootstrap_servers='localhost:29092')

print("Listening")
while True:
    for message in consumer:
        print("Here comes a message..")
        print (message)