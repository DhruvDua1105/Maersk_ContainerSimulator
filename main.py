import simpy
import random


class Vessel:
    def __init__(self, env, name, terminal, arrival_interval):
        self.env = env
        self.name = name
        self.terminal = terminal
        self.arrival_interval = arrival_interval
        self.containers = 150
        self.action = env.process(self.arrive())

    def arrive(self):
        yield self.env.timeout(random.expovariate(1 / self.arrival_interval))  # Adjusted time between arrivals
        print(f'Minute no: {self.env.now}: {self.name} arrives at the terminal.')

        with self.terminal.berths.request() as berth_request:
            yield berth_request
            print(f'Minute no: {self.env.now}: {self.name} berths.')

            yield self.env.process(self.unload())

    def unload(self):
        with self.terminal.cranes.request() as crane_request:
            yield crane_request
            print(f'Minute no: {self.env.now}: Crane starts unloading {self.name}.')

            for i in range(self.containers):  # 150 containers in each vessel
                with self.terminal.trucks.request() as truck_request:
                    yield truck_request
                    print(f'Minute no: {self.env.now}: Truck starts transporting container {i + 1} from {self.name}.')
                    yield self.env.timeout(3)  # Crane unloads a container in 3 minutes
                    yield self.env.timeout(6)  # Truck takes 6 minutes to drop off the container
                    print(
                        f'Minute no: {self.env.now}: Truck returns after delivering container {i + 1} from {self.name}.')

            print(f'Minute no: {self.env.now}: {self.name} has finished unloading and leaves the berth.')


class Terminal:
    def __init__(self, env, num_berths, num_cranes, num_trucks):
        self.env = env
        self.berths = simpy.Resource(env, num_berths)
        self.cranes = simpy.Resource(env, num_cranes)
        self.trucks = simpy.Resource(env, num_trucks)


def run_simulation(simulation_time, average_arrival_interval):
    env = simpy.Environment()
    terminal = Terminal(env, num_berths=2, num_cranes=2, num_trucks=3)

    # Create initial vessels to start simulation with adjusted arrival intervals
    for i in range(50):  # Replace the number 4 with the number of vessels you want
        Vessel(env, f'Vessel {i + 1}', terminal, average_arrival_interval)

    env.run(until=simulation_time)


if __name__ == "__main__":
    # Enter the simulation time
    simulation_time = int(input("Enter the simulation time (in minutes): "))

    # Adjust the average time between vessel arrivals based on the simulation time
    if simulation_time < 300:  # If the simulation time is less than 5 hours
        average_arrival_interval = simulation_time / 6  # Aim for roughly 6 vessel arrivals within the simulation time
    else:
        average_arrival_interval = 300  # Default to 5 hours if the simulation time is long enough

    run_simulation(simulation_time, average_arrival_interval)
