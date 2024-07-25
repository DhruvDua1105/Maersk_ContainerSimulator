# Simulating a container terminal using SimPy

This project simulates the operations of a container terminal using the SimPy library. The simulation includes vessels arriving at the terminal, berthing, unloading containers using quay cranes, and transporting containers using terminal trucks.

## Screenshots
![image](https://github.com/user-attachments/assets/2ede83db-37e8-4737-b7ce-85d13e33f295)


## Features

- Simulates vessel arrivals following an exponential distribution.
- Each vessel carries 150 containers that need to be discharged.
- The terminal has 2 berths, 2 quay cranes, and 3 terminal trucks.
- Vessels berth at the terminal and are unloaded by quay cranes.
- Containers are transported by trucks to yard blocks.
- Includes detailed logging of each event with timestamps.

## Requirements

- Python 3.x
- SimPy library

## Installation

1. Clone the repository
2. Install the required library using pip:
   
    ```bash
    pip install simpy
    ```

## Usage

1. Run the script:
   
    ```bash
    python main.py
    ```

3. When prompted, enter the simulation time in minutes.

