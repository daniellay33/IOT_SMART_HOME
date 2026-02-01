import paho.mqtt.client as mqtt
import json
import time

MQTT_BROKER = "mosquitto"
MQTT_PORT = 1883
TOPIC_SENSORS = "home/security/sensors"
TOPIC_CONTROL = "home/security/control"
TOPIC_ALERTS = "home/security/alerts"

class DataManager:
    def __init__(self):
        self.is_armed = False 
        self.client = mqtt.Client("DataManager")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT Broker")
            self.client.subscribe(TOPIC_SENSORS)
            self.client.subscribe(TOPIC_CONTROL)
        else:
            print(f"Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        
        if msg.topic == TOPIC_CONTROL:
            new_state = payload.get("state")
            if new_state == "ARM":
                self.is_armed = True
                print(">>> System ARMED")
            elif new_state == "DISARM":
                self.is_armed = False
                print(">>> System DISARMED")

        elif msg.topic == TOPIC_SENSORS:
            sensor_type = payload.get("type")
            status = payload.get("status")
            print(f"Log: Sensor {sensor_type} reported {status}")

            if self.is_armed and status == "ALERT":
                self.trigger_alarm(sensor_type)

    def trigger_alarm(self, sensor_source):
        alert_msg = {
            "event": "INTRUSION_DETECTED",
            "source": sensor_source,
            "timestamp": time.ctime(),
            "action": "SIREN_ON"
        }
        self.client.publish(TOPIC_ALERTS, json.dumps(alert_msg))
        print(f"!!! ALARM TRIGGERED by {sensor_source} !!!")

    def run(self):
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.loop_forever()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    manager = DataManager()
    manager.run()