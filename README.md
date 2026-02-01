🏠 Smart Home Security System

MQTT · Python · Docker

This project is a Smart Home Security System simulator built with Python, MQTT, and Docker.
It demonstrates an event-driven IoT architecture where independent services communicate through a message broker using the publish/subscribe model.

📌 Overview

The system simulates a home security environment with virtual sensors, centralized logic, and a user interface.

All components are decoupled and communicate only via MQTT topics, closely resembling real-world IoT systems.

🏗 System Architecture
+------------------+        MQTT        +-------------------+
| Sensor Emulator  |  ─────────────▶  |                   |
| (Docker)         |                   |                   |
+------------------+                   |                   |
                                       |   Mosquitto       |
+------------------+        MQTT        |   MQTT Broker     |
| GUI Application  |  ◀────────────▶  |   (Docker)        |
| (Host Machine)  |                   |                   |
+------------------+                   |                   |
                                       |                   |
+------------------+        MQTT        |                   |
| Data Manager     |  ◀────────────▶  |                   |
| (Docker)         |                   +-------------------+
+------------------+

🧩 Components
🔹 Sensor Emulator (sensor_emulator.py)

Runs inside a Docker container

Simulates home security sensors (motion, door events, etc.)

Periodically publishes sensor data to:

home/security/sensors

🔹 Data Manager (data_manager.py)

Runs inside a Docker container

Acts as the system’s central logic

Subscribes to:

home/security/sensors

home/security/control

Maintains system state (ARM / DISARM)

Publishes security alerts to:

home/security/alerts

🔹 GUI Application (gui_app.py)

Runs on the host machine (outside Docker)

Built using Tkinter

Allows the user to:

Arm and disarm the security system

Receive real-time alert notifications

Connects to the MQTT broker via:

localhost:1883

🔹 MQTT Broker (Mosquitto)

Runs inside a Docker container

Image: eclipse-mosquitto

Exposed ports:

1883 – MQTT

9001 – MQTT over WebSockets

📡 MQTT Topics
Topic	Purpose
home/security/sensors	Sensor data published by the emulator
home/security/control	Control commands (ARM / DISARM)
home/security/alerts	Alerts sent to the GUI application
🐳 Docker Setup
Build and start all containers:
docker compose up --build


This will start:

Mosquitto MQTT broker

Sensor emulator service

Data manager service

🖥 Running the GUI Application

The GUI is executed outside Docker on the host machine.

1️⃣ Install dependencies:
pip install -r requirements.txt

2️⃣ Run the GUI:
python gui_app.py


⚠️ Make sure Docker is running and all containers are up before launching the GUI.

🛠 Requirements

Python 3.9+

Docker & Docker Compose

MQTT (Mosquitto broker via Docker)

Python libraries:

paho-mqtt

tkinter

🎯 Key Concepts Demonstrated

MQTT publish/subscribe messaging

Event-driven architecture

Service decoupling

IoT system simulation

Docker networking and container communication

Stateful backend logic
