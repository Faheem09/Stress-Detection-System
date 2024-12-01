# Stress Detection System

This project demonstrates how to detect stress using data from multiple sensors (heart rate, skin temperature, galvanic skin response) and Python.

## Features
- Real-time data collection using Arduino
- Stress detection using Python and Isolation Forest
- Visualization of detected stress levels

## Hardware Requirements
- Arduino-compatible board (e.g., Arduino Nano)
- Sensors:
  - Heart Rate Monitor
  - Temperature Sensor
  - Galvanic Skin Response (GSR) Sensor
- USB Cable
- PC with Python and VS Code

## Software Requirements
- Arduino IDE
- Python 3.7 or higher
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `pyserial`

## Setup Instructions

### Arduino Setup
1. Upload the `Stress_Sensor.ino` sketch to the Arduino.
2. Connect the Arduino to your PC.

### Python Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Stress-Detection-System.git
   cd Stress-Detection-System
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scriptsctivate
   pip install -r requirements.txt
   ```
3. Run the `data_collection.py` script to collect stress data:
   ```bash
   python Python_Code/data_collection.py
   ```
4. Run the `stress_detection.py` script to detect stress levels:
   ```bash
   python Python_Code/stress_detection.py
   ```

## Example Visualization
![Stress Detection Plot](example_plot.png)

## License
This project is licensed under the MIT License.
