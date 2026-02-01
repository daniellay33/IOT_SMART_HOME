import tkinter as tk
from tkinter import messagebox
import paho.mqtt.client as mqtt
import json
import threading

MQTT_BROKER = "mosquitto" 
MQTT_PORT = 1883
TOPIC_CONTROL = "home/security/control"
TOPIC_ALERTS = "home/security/alerts"

class SecurityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home Security Dashboard")
        self.root.geometry("400x400")
        self.root.configure(bg="#2c3e50")

      
        self.label = tk.Label(root, text="Security System Control", font=("Arial", 18, "bold"), fg="white", bg="#2c3e50")
        self.label.pack(pady=20)

        self.arm_btn = tk.Button(root, text="ARM SYSTEM", command=self.arm_system, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), width=15)
        self.arm_btn.pack(pady=10)

        self.disarm_btn = tk.Button(root, text="DISARM SYSTEM", command=self.disarm_system, bg="#27ae60", fg="white", font=("Arial", 12, "bold"), width=15)
        self.disarm_btn.pack(pady=10)

      
        self.status_label = tk.Label(root, text="System Status: Ready", font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
        self.status_label.pack(pady=20)

        self.log_list = tk.Listbox(root, height=5, width=40, bg="#34495e", fg="#f1c40f")
        self.log_list.pack(pady=10)

        self.client = mqtt.Client("SecurityGUI")
        self.client.on_message = self.on_message
        
        threading.Thread(target=self.mqtt_thread, daemon=True).start()

    def mqtt_thread(self):
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.subscribe(TOPIC_ALERTS)
            self.client.loop_forever()
        except:
            self.status_label.config(text="Status: Broker Offline", fg="red")

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        if msg.topic == TOPIC_ALERTS:
            event = payload.get("event")
            source = payload.get("source")
            self.log_list.insert(0, f"!!! {event} from {source} !!!")
            messagebox.showwarning("SECURITY ALERT", f"Intrusion detected from {source}!")

    def arm_system(self):
        self.client.publish(TOPIC_CONTROL, json.dumps({"state": "ARM"}))
        self.status_label.config(text="System Status: ARMED", fg="#e74c3c")

    def disarm_system(self):
        self.client.publish(TOPIC_CONTROL, json.dumps({"state": "DISARM"}))
        self.status_label.config(text="System Status: DISARMED", fg="#27ae60")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityGUI(root)
    root.mainloop()