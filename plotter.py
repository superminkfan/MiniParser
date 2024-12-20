# plotter.py

import matplotlib.pyplot as plt

def plot_metrics(records, output_prefix="ignite_metrics"):
    """
    Plot various metrics from the records and save the figures as PNG files.

    :param records: list of dict with cleaned numeric data and timestamps
    :param output_prefix: str, prefix for output file names
    """
    # Extract lists for plotting
    timestamps = [r["timestamp"] for r in records]

    # CPU metrics
    curLoad = [r["curLoad"] for r in records]
    avgLoad = [r["avgLoad"] for r in records]

    # Heap metrics
    heapUsed = [r["heapUsed"] for r in records]
    heapFree = [r["heapFree"] for r in records]

    # Default region metrics
    defaultUsedRam = [r["defaultUsedRam"] for r in records]
    defaultFreeRam = [r["defaultFreeRam"] for r in records]

    # Plot CPU loads
    plt.figure(figsize=(10,5))
    plt.plot(timestamps, curLoad, label="Cur Load (%)", marker='o')
    plt.plot(timestamps, avgLoad, label="Avg Load (%)", marker='o')
    plt.xlabel("Time")
    plt.ylabel("Load (%)")
    plt.title("CPU Load Over Time")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_cpu_load.png")
    plt.close()

    # Plot Heap metrics
    plt.figure(figsize=(10,5))
    plt.plot(timestamps, heapUsed, label="Heap Used (MB)", marker='o', color='red')
    plt.xlabel("Time")
    plt.ylabel("Heap Used (MB)")
    plt.title("Heap Usage Over Time")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_heap_used.png")
    plt.close()

    plt.figure(figsize=(10,5))
    plt.plot(timestamps, heapFree, label="Heap Free (%)", marker='o', color='green')
    plt.xlabel("Time")
    plt.ylabel("Heap Free (%)")
    plt.title("Heap Free Over Time")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_heap_free.png")
    plt.close()

    # Plot Default region metrics
    plt.figure(figsize=(10,5))
    plt.plot(timestamps, defaultUsedRam, label="Default Used Ram (MB)", marker='o', color='purple')
    plt.xlabel("Time")
    plt.ylabel("Used Ram (MB)")
    plt.title("Default Region Used Ram Over Time")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_default_used_ram.png")
    plt.close()

    plt.figure(figsize=(10,5))
    plt.plot(timestamps, defaultFreeRam, label="Default Free Ram (%)", marker='o', color='orange')
    plt.xlabel("Time")
    plt.ylabel("Free Ram (%)")
    plt.title("Default Region Free Ram Over Time")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_prefix}_default_free_ram.png")
    plt.close()
