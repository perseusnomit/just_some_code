import psutil
import matplotlib.pyplot as plt

# Lists to store the recorded RAM usage
timestamps = []
ram_usage = []

# Function to record RAM usage
def record_ram_usage():
    # Get the current timestamp
    timestamp = psutil.cpu_times().user

    # Get the current RAM usage
    ram = psutil.virtual_memory().used

    # Append the timestamp and RAM usage to the lists
    timestamps.append(timestamp)
    ram_usage.append(ram)

# Record RAM usage at regular intervals
interval = 1  # in seconds
while True: #endless loop
    record_ram_usage()
    plt.plot(timestamps, ram_usage)
    plt.xlabel('Time')
    plt.ylabel('RAM Usage')
    plt.title('RAM Usage Over Time')
    plt.pause(interval)

#save the graph to a file
plt.savefig('ram_usage_graph.png')
