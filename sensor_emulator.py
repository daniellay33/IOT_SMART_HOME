import paho.mqtt.client as mqtt
import json
import time
import random

MQTT_BROKER = "mosquitto"
MQTT_PORT = 1883
TOPIC_SENSORS = "home/security/sensors"

class SensorEmulator:
    def __init__(self):
        self.client = mqtt.Client("SensorEmulator")

    def connect(self):
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            print(f"Connected to MQTT Broker at {MQTT_BROKER}")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def publish_sensor_data(self, sensor_type, status):
        """שליחת נתוני חיישן בפורמט JSON"""
        payload = {
            "type": sensor_type,
            "status": status,
            "timestamp": time.time(),
            "location": "Main Entrance"
        }
        self.client.publish(TOPIC_SENSORS, json.dumps(payload))
        print(f" [Sensor] {sensor_type} sent: {status}")

    def run_simulation(self):
        """סימולציה של אירועי אבטחה אקראיים"""
        sensors = ["Motion_PIR", "Magnetic_Door"]
        
        while True:
            selected_sensor = random.choice(sensors)
            current_status = "ALERT" if random.random() < 0.2 else "OK"
            self.publish_sensor_data(selected_sensor, current_status)
            
            
            time.sleep(5)

if __name__ == "__main__":
    emulator = SensorEmulator()
    emulator.connect()
    print("Starting Sensor Simulation... (Press Ctrl+C to stop)")
    emulator.run_simulation()