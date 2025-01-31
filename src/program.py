import paho.mqtt.client as mqtt
import random
import time
import json

# Detalii broker MQTT
broker = "localhost"  # Sau adresa IP a brokerului Mosquitto
port = 1883
topic = "senzor"

# Funcția care va fi apelată când se conectează clientul la broker
def on_connect(client, userdata, flags, rc):
    print(f"Conectat la broker MQTT cu codul {rc}")

# Inițializarea clientului MQTT
client = mqtt.Client()

# Setează funcția de conectare
client.on_connect = on_connect

# Conectare la broker
client.connect(broker, port, 60)

# Rulează un loop de conectare
client.loop_start()

while True:
    # Generează temperatură aleatorie între -10 și 35 grade Celsius
    temp = round(random.uniform(-10, 35), 2)

    # Generează umiditate aleatorie între 30% și 90%
    humidity = round(random.uniform(30, 90), 2)

    # Creează un obiect JSON cu datele generate
    data = {
        "temperature": temp,
        "humidity": humidity
    }

    # Publică mesajul pe topicul "senzoe"
    client.publish(topic, json.dumps(data))

    print(f"Trimis la topicul '{topic}': {data}")

    # Așteaptă 5 secunde înainte de a trimite următoarele date
    time.sleep(5)
