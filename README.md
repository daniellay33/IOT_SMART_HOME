# 🏠 Smart Home Security System

A smart home security system simulator built with **Python**, **MQTT**, and **Docker**.  
This project demonstrates an **event-driven IoT architecture** using the publish/subscribe messaging model.

---

## Overview

The system simulates a home security environment with virtual sensors, centralized decision logic, and a graphical user interface.

All components are **decoupled** and communicate **only through MQTT topics**, similar to real-world IoT systems.

---

## Architecture

- **Sensor Emulator** publishes sensor events
- **Data Manager** processes events and system state
- **GUI Application** controls the system and displays alerts
- **MQTT Broker (Mosquitto)** acts as the communication layer

**Runtime locations:**
- Sensors, Data Manager, and MQTT Broker run in Docker containers
- GUI Application runs on the host machine

---

## Components

### Sensor Emulator (`sensor_emulator.py`)
- Runs inside a Docker container
- Simulates motion and door sensors
- Publishes sensor data to:
home/security/sensors


---

### Data Manager (`data_manager.py`)
- Runs inside a Docker container
- Acts as the system’s central logic
- Subscribes to:
- `home/security/sensors`
- `home/security/control`
- Maintains system state (ARM / DISARM)
- Publishes alerts to:
home/security/alerts


---

### GUI Application (`gui_app.py`)
- Runs on the host machine (outside Docker)
- Built using Tkinter
- Allows the user to:
- Arm and disarm the security system
- Receive real-time alerts
- Connects to the MQTT broker via:
localhost:1883


---

### MQTT Broker
- Uses **Mosquitto**
- Runs inside a Docker container
- Exposed ports:
- `1883` – MQTT
- `9001` – MQTT over WebSockets

---

## MQTT Topics

| Topic | Description |
|------|------------|
| `home/security/sensors` | Sensor data |
| `home/security/control` | Control commands (ARM / DISARM) |
| `home/security/alerts` | Security alerts |

---

## Getting Started

### 1. Start backend services
```bash
docker compose up --build
This starts:

Mosquitto MQTT broker

Sensor emulator

Data manager

2. Run the GUI application
python gui_app.py
⚠️ Ensure Docker is running and all containers are up before starting the GUI.

Requirements
Python 3.9+

Docker & Docker Compose

MQTT (Mosquitto)

Python packages:

paho-mqtt

tkinter

Key Concepts Demonstrated
MQTT publish/subscribe messaging

Event-driven architecture

Service decoupling

IoT system simulation

Docker networking

