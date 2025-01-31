# Temperature and Humidity Monitoring

## Overview

This project enhances a simpler version that only supported local network communication without a dashboard. Now, with the integration of Node-RED, users can monitor and interact with sensor data via an intuitive interface.
Course: Internet of Things


![image](https://github.com/user-attachments/assets/827ad802-566e-4a2f-8514-887fff1482b4)


## Software Requirements

- PlatformIO (preferred) or Arduino IDE
- Mosquitto MQTT Broker
- Node-RED

## Setup and Installation


1. **Software Setup**: 
   - Install and setup VSCode + PlatformIO (preferred) or Arduino IDE.
   - Install Mosquitto MQTT Broker.
   - Install Node-RED.
   - Install Node-RED Dashboard.
  

![Screenshot 2025-01-31 201835](https://github.com/user-attachments/assets/7e6ea516-8d41-47d8-8f2a-501e3b6ba475)

## Running the Project

1. Start the Mosquitto broker.
2. Start Node-RED and open the provided dashboard.
3. Start the python code.
4. Open the https provided in terminal after running node-red
5. Open the dashboard by modifying the link (should be something like this http://127.0.0.1:1880/ui/)

## MQTT Broker

Download and install the Mosquitto MQTT Broker from [here](https://mosquitto.org/download/).
You can start the broker with the default configuration by running `mosquitto` in the terminal.

## Node-RED

Download and install Node-RED from [here](https://nodered.org/docs/getting-started/local).
You can start Node-RED by running `node-red` in the terminal.

![Node-RED Flow](https://imgur.com/jv2cUAx.png)



## Node-RED Dashboard

Install the Node-RED Dashboard from [here](https://flows.nodered.org/node/node-red-dashboard).
You can access the dashboard by going to `http://localhost:1880/ui` in your browser.

![Node-RED Dashboard](https://imgur.com/XGUOuPg.png)


![iot2](https://github.com/user-attachments/assets/37060d62-2980-496f-87a0-d595130d957a)


## Considerations

PlatformIO is recommended for its advanced features, including code completion and linting.


