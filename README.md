Smart Home Security System - IoT Project
A modular, event-driven IoT security system designed for smart home environments. This project utilizes a Microservices Architecture to monitor sensors, manage security states, and provide real-time alerts.

🚀 Key Features
Real-Time Intrusion Detection: Instant alerts from motion and door sensors via MQTT.

Remote Management: Toggle system security states (Armed/Disarmed) through a central dashboard.

Containerized Infrastructure: Entire stack (Broker, Logic, Database, Sensors) managed via Docker.

Event Logging: Historical data of all security events stored for audit and monitoring.

🛠 Tech Stack
Language: Python 3.x

Communication: MQTT Protocol (Eclipse Paho)

Message Broker: Mosquitto MQTT

Orchestration: Docker & Docker Compose

Database: SQLite / In-memory Log System

🏗 System Architecture
The system consists of several independent services running in separate Docker containers:

MQTT Broker: The central hub for message distribution.

Sensor Emulator: Simulates physical door and motion sensors.

Data Manager (Core Logic): Processes incoming data and decides when to trigger alarms based on the system state.

Dashboard/GUI: Provides a user interface for monitoring and control.

🚦 Getting Started
Prerequisites
Docker and Docker Compose installed on your machine.

Installation & Execution
Clone the repository:

Bash
git clone https://github.com/your-username/smart-home-security.git
cd smart-home-security
Launch the entire system using Docker Compose:

Bash
docker-compose up --build
Access the logs to see the communication flow between sensors and the broker.

📊 Work Flow
The system follows an asynchronous event-driven flow:

Sensor publishes state to home/security/sensors.

Data Manager subscribes to the topic and evaluates the logic.

If State == Armed and Sensor == Alert, an alarm command is published to home/security/alerts.

📜 License
This project was developed as part of the IoT Software Development course at HIT.
