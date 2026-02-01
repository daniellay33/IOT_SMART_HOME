# Smart Home Security System

This project simulates a smart home security system using Python, MQTT, and Docker.

## Components
- Sensor Emulator: simulates motion and door sensors
- Data Manager: processes sensor data and system state
- GUI Application: allows arming/disarming and shows alerts
- MQTT Broker (Mosquitto): message broker between all components

## How it works
- Sensors publish data to MQTT
- Data Manager processes the data
- GUI sends control commands and receives alerts

## Running the project
1. Start the backend services:
   ```bash
   docker compose up --build
